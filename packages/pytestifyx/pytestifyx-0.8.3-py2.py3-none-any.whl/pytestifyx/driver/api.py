import copy
import importlib
import json
import concurrent.futures

from requests_toolbelt import MultipartEncoder
import requests
from typing import Dict

from pytestifyx.utils.json.core import json_update
from pytestifyx.utils.logs.core import log
from pytestifyx.utils.public.extract_url import extract_url, restore_url
from pytestifyx.utils.parse.config import parse_yaml_config
from pytestifyx.utils.requests.reload_all import reload_all
from pytestifyx.utils.requests.requests_config import Config

import inspect
import functools

MODULES = ['body', 'headers', 'url']
FUNC_NAME_PREFIX = 'test_'
FUNC_NAME_SUFFIX = '_path_params'


class APIRequestMeta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        for attr_name, attr_value in attrs.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                setattr(new_cls, attr_name, cls.generate_api_method(attr_name, attr_value))
        return new_cls

    @staticmethod
    def generate_api_method(name, func):
        @functools.wraps(func)
        def wrapped_func(self, param=None, config: Config = Config(), **kwargs):
            if param is None:
                param = {}
            method_doc = inspect.getdoc(func)
            notes = method_doc.split('\n')[0].strip() if method_doc else "Unknown request"
            log.info(f'--------------{notes}-----------------')
            api_class_file = inspect.getmodule(self).__file__

            response = self.api(api_class_file, name, param, config, **kwargs)
            return response

        return wrapped_func


def get_template_value(template, func_name: str):
    if func_name.startswith(FUNC_NAME_PREFIX):
        func_name = func_name.replace(FUNC_NAME_PREFIX, '')
    try:
        if hasattr(template, func_name):
            if template.__getattribute__(func_name) is not None:
                return template.__getattribute__(func_name)
            else:
                return {}
        else:
            return {}
    except AttributeError:
        log.warning(f'请配置{func_name}模版参数')


class Context:
    def __init__(self, headers, data, url, query_params):
        self.headers = headers
        self.data = data
        self.url = url
        self.query_params = query_params


class BaseRequest:

    def base(self, path, func_name, params, config: Config, **kwargs):
        # 解析配置参数
        api_config = parse_yaml_config('config.yaml')

        templates = self.base_init_module(path, api_module_name=api_config['api_module']['api_module_name'])

        if 'delete_key' in params:
            config.delete_key = params['delete_key']

        # 解析模版参数
        url, headers, data, query_params, templates = self.base_init_prepare_request(api_config, config, templates, func_name)

        # 创建一个新的 Context 实例
        context = Context(headers, data, url, query_params)

        # 创建 HookedRequest 实例，所有钩子类将自动注册
        generate_parameters_hook_params = {"params": params, "context": context, "templates": templates, "func_name": func_name}
        send_requests_hook_params = {"context": context, "templates": templates, "func_name": func_name}
        hooks_params = [
            (GenerateParametersHook, generate_parameters_hook_params, 0),
            (SendRequestHook, send_requests_hook_params, 0),
        ]
        hooked_request = HookedRequest(config, hooks_params)
        results = hooked_request.execute_hooks()
        # 处理钩子函数返回值
        all_hooks_results = {}
        for hook_name, result in results.items():
            all_hooks_results[hook_name] = result
        return all_hooks_results['SendRequestHook'].response

    def base_init_module(self, path: str, api_module_name='api_test') -> dict:
        import_path = path.split(api_module_name)[1].split('core.py')[0]
        templates = {module: self.import_template(import_path, module, api_module_name) for module in MODULES}
        return templates

    def base_init_prepare_request(self, api_config, config, templates: dict, func_name: str):
        url_prefix = api_config['url_prefix'][config.env_name]
        path = get_template_value(templates['url'], config.request_method.upper() + '_' + func_name)
        url = url_prefix + path
        custom_header = get_template_value(templates['headers'], func_name + '_headers')
        headers = custom_header if custom_header else get_template_value(templates['headers'], 'headers')
        data = get_template_value(templates['body'], config.request_method.upper() + '_' + func_name)
        query_params = get_template_value(templates['body'], config.request_method.upper() + '_' + func_name + '_query_params')
        return url, copy.deepcopy(headers), copy.deepcopy(data), copy.deepcopy(query_params), templates

    @staticmethod
    def import_template(path: str, module_name: str, api_module_name='api_test'):
        import_module_body = path.replace('\\', '.').replace('/', '.') + module_name
        template_body = importlib.import_module(import_module_body, api_module_name)
        return template_body

    @staticmethod
    def reload_template(reload_config, module):
        if reload_config:
            reload_all(module)


class HookMeta(type):
    def __new__(cls, name, bases, attrs):
        new_cls = super().__new__(cls, name, bases, attrs)
        new_cls.is_hook = True
        return new_cls


def create_hook_instance(config, hook_cls, params, hook_instances):
    hook_cls_name = hook_cls.__name__
    if hook_cls_name not in hook_instances:
        hook_instances[hook_cls_name] = hook_cls(config, **params)
    return hook_instances[hook_cls_name]


class HookWrapper:
    def __init__(self, config, hook_cls, params, priority=0):
        self.config = config
        self.hook_cls = hook_cls
        self.params = params
        self.priority = priority

    def __call__(self, hook_instances):
        hook_instance = create_hook_instance(self.config, self.hook_cls, self.params, hook_instances)
        hook_instances[self.hook_cls.__name__] = hook_instance
        return hook_instance


class Hook(metaclass=HookMeta):
    def __init__(self, config, priority=0):
        self.config = config
        self.priority = priority

    def should_execute(self):
        raise NotImplementedError()

    def execute(self, **kwargs):
        raise NotImplementedError()


class HookedRequest:
    def __init__(self, config, hooks_params):
        self.config = config
        self.hook_instances = {}  # 将原来的列表类型修改为字典类型
        for hook_cls, params, priority in hooks_params:
            HookWrapper(config, hook_cls, params, priority=priority)(self.hook_instances)

        # 根据优先级从高到低排序钩子实例列表
        self.hook_instances = dict(sorted(self.hook_instances.items(), key=lambda x: x[1].priority))

    def execute_hooks(self, **kwargs) -> Dict[str, any]:
        results = {}
        for hook_name, hook_instance in self.hook_instances.items():
            if hook_instance.should_execute():
                result = hook_instance.execute(**kwargs)
                results[hook_name] = result
        return results


class GenerateParametersHook(Hook):
    def __init__(self, config, params, context, templates, func_name, priority=0):
        super().__init__(config, priority)
        self.params = params
        self.context = context
        self.templates = templates
        self.func_name = func_name

    def should_execute(self):
        return True

    def execute(self):
        # 处理删除的key
        for key in self.config.delete_key:
            if key in self.context.data:
                self.context.data.pop(key)

        # 特殊处理请求头
        if '_headers' in self.params:
            self.context.headers.update(self.params['_headers'])

        # 特殊处理url中的参数
        pk_params = extract_url(self.context.url)
        json_update(pk_params, self.params)
        self.context.url = restore_url(self.context.url, pk_params)

        # 处理请求参数query_params
        json_update(self.context.query_params, self.params)

        # 处理入参为list的情况
        if isinstance(self.context.data, list):
            self.context.data = {'_data_': self.context.data}

        # 处理请求头同名字段覆
        if self.config.is_cover_header:
            json_update(self.context.headers, self.context.data)  # 入参同名字段替换请求头

        json_update(self.context.data, self.params)
        # 还原入参为list的情况
        if isinstance(self.context.data, dict) and '_data_' in self.context.data:
            self.context.data = self.context.data['_data_']
        return self.context


class ConcurrentRequests:
    def __init__(self, max_workers=5):
        self.max_workers = max_workers

    def send_requests(self, hook_instance, request_method):
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(hook_instance.make_request, request_method) for _ in range(self.max_workers)]
            for future in concurrent.futures.as_completed(futures):
                try:
                    results.append(future.result())
                except Exception as exc:
                    print(f'Generated an exception: {exc}')
        return results


class SendRequestHook(Hook):
    def __init__(self, config, context, templates, func_name, priority=0):
        super().__init__(config, priority)
        self.context = context
        self.templates = templates
        self.func_name = func_name
        self.session = requests.Session()
        self.session.verify = False

    def should_execute(self):
        return True

    def execute(self):

        log.info(f'----------------请求头为{json.dumps(self.context.headers, indent=4, ensure_ascii=False)}')
        log.info(f'----------------请求参数为{json.dumps(self.context.query_params, indent=4, ensure_ascii=False)}')
        req = requests.models.PreparedRequest()
        req.prepare_url(self.context.url, self.context.query_params)
        log.info(f'----------------请求地址为{req.url}')
        request_method = self.config.request_method.upper()
        log.info(f'----------------请求方式为{request_method}---------------')

        if self.config.concurrent_number > 1:
            # 执行并发请求
            concurrent_requests = ConcurrentRequests(self.config.concurrent_number)
            response = concurrent_requests.send_requests(self, self.config.request_method.upper())
            for i in response:
                self.handle_response(i)
        else:
            # 执行单个请求
            response = self.make_request(self.config.request_method.upper())
            self.handle_response(response)

        class Parameters:
            def __init__(self, response):
                self.response = response

        return Parameters(response)

    def make_request(self, request_method):
        if self.func_name.startswith(FUNC_NAME_PREFIX):
            self.func_name = self.func_name.replace(FUNC_NAME_PREFIX, '')

        # 请求方式处理 POST/PUT/GET/DELETE
        if request_method in ['POST', 'PUT', 'GET']:
            if self.config.content_type.upper() == 'JSON':
                self.context.headers['Content-Type'] = 'application/json'
            elif self.config.content_type == 'multipart/form-data':  # 处理文件上传
                m = MultipartEncoder(fields=self.context.data)
                self.context.headers['Content-Type'] = m.content_type
                self.context.data = m
            else:
                raise Exception('暂不支持的Content-Type')

        # 请求打印日志处理
        log.info(f'----------------开始打印请求日志-----------------')
        if self.config.is_request_log:
            if self.config.is_request_log_json_dumps:
                log.info('----------------请求体原始报文' + json.dumps(self.context.data, indent=4, ensure_ascii=False))
            else:
                log.info('----------------请求体原始报文' + str(self.context.data))
        else:
            log.info('----------------请求体原始报文日志配置为不打印-----------------')

        # 请求处理
        log.info(f'----------------发送请求 🚀 -----------------')
        if self.context.data:
            if request_method in ['GET', 'DELETE']:
                return self.session.request(request_method, self.context.url, headers=self.context.headers, params=self.context.query_params, timeout=60)
            else:
                if self.config.is_json_dumps and self.config.content_type.upper() == 'JSON':
                    return self.session.request(request_method, self.context.url, headers=self.context.headers, params=self.context.query_params, json=self.context.data, timeout=60)
                else:
                    return self.session.request(request_method, self.context.url, headers=self.context.headers, params=self.context.query_params, data=self.context.data, timeout=60)
        else:
            if self.config.is_json_dumps:
                return self.session.request(request_method, self.context.url, headers=self.context.headers, params=self.context.query_params, json=self.context.data, timeout=60)
            else:
                return self.session.request(request_method, self.context.url, headers=self.context.headers, params=self.context.query_params, data=self.context.data, timeout=60)

    def handle_response(self, response):
        log.info(f'----------------接口的响应码：{response.status_code}')
        log.info('----------------接口的响应时间为：' + str(response.elapsed.total_seconds()))
        # 返回打印日志处理
        log.info(f'----------------开始打印返回日志-----------------')
        if self.config.is_response_log:
            if self.config.is_response_log_json_dumps:
                log.info('----------------返回报文' + json.dumps(response.json(), indent=4, ensure_ascii=False))
            else:
                log.info('----------------返回报文' + str(response.json()))
        else:
            log.info('----------------返回报文日志配置为不打印-----------------')
