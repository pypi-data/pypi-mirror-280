#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'andy.hu'
__mtime__ = '2021/07/09'

"""
import os
import re
import time
import threading
import json
from typing import Any, Callable, List, Optional, Set, Union

from fastapi import FastAPI, APIRouter, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRoute
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request as HttpRequest
from starlette.responses import Response as HttpResponse

from clife_svc.libs import utils
from clife_svc.libs.context import request_id, app_id
from clife_svc.config.disconf import Disconf
from clife_svc.config.configmap import ConfigMap
from clife_svc.errors.error_code import ApiException
from clife_svc.libs.http_request import ClientRequest
from clife_svc.libs.log import init_log, klogger, plogger
from clife_svc.libs.mq_handler import MQHandler


class AiServiceRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            logger = plogger if request.scope['path'] == '/time' else klogger

            body = await request.body()
            if request.query_params:
                logger.info('Request Params: {}'.format(request.query_params))
            if body:
                try:
                    logger.info('Request Body: {}'.format(json.loads(body.decode('utf-8'))))
                except:
                    logger.info('Request Body: {}'.format(body.decode('utf-8')))
            before = time.time()
            response: Response = await original_route_handler(request)
            logger.info('Request Cost: {}s'.format(round(time.time() - before, 2)))
            if hasattr(response, 'body'):
                logger.info('Response Content: {}'.format(response.body.decode('utf-8')))
            return response

        return custom_route_handler


class App(object):
    """
    http接口服务上下文对象，单实例对象
    """
    _instance = None
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        实现单例模式
        """
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, app_name: str, log_root_path: str = '/www/logs', conf: Union[str, list] = '', log_level: str = 'DEBUG'):
        """
        构造函数
        :param app_name 项目名称
        :param log_root_path 项目输出的日志根路径，推荐使用/www/logs，便于线上统一采集日志
        :param conf: 配置文件名称列表，提供字符串列表或逗号分隔字符串
        :param log_level: 日志收集器级别，从低到高依次为 TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL
        """

        # app_name参数校验

        if not re.match(r'^([a-zA-Z0-9]+-?[a-zA-Z0-9]+)+$', app_name):
            raise Exception('app_name can only be letters, numbers, or strike-through!')

        self.app_name = app_name
        init_log(os.path.join(log_root_path, app_name), log_level=log_level)

        self.__disconf = Disconf('clife-ai', '0.0.1-SNAPSHOT', conf).get_disconf()
        self.__configmap = ConfigMap()

        self.__client = ClientRequest(self)
        self.__mq_handler = MQHandler(self)

        self.__fast_api = FastAPI(title='ai-service', default_response_class=ORJSONResponse)
        self.__ai_router = APIRouter(route_class=AiServiceRoute)

    def init_api(self) -> FastAPI:
        """
        在App中初始化服务接口
        :return: FastAPI，作为服务器运行入口对象
        """
        self.__init_middlewares()
        self.__fast_api.add_exception_handler(ApiException, api_exception_handler)
        self.__fast_api.add_exception_handler(Exception, app_exception)
        self.__ai_router.add_api_route('/time', endpoint=probe, methods=['GET'], name='time')
        self.__fast_api.include_router(self.__ai_router)
        self.__mq_handler.start_consumer()
        return self.__fast_api

    def __init_middlewares(self):
        self.__fast_api.add_middleware(CORSMiddleware,
                                       allow_credentials=True,
                                       allow_origins=["*"],
                                       allow_methods=["*"],
                                       allow_headers=["*"], )
        self.__fast_api.add_middleware(Interceptor)

    def get_conf(self, key: str, default: str = '') -> str:
        if key in self.__disconf:
            return self.__disconf.get(key)
        item = self.__configmap.get(key)
        if item:
            return item
        item = utils.get_env(key)
        if item:
            return item
        return default

    def get_conf_list(self, key: str, default: list = None) -> list:
        """
        获取列表形式配置数据
        :param key:配置项的key
        :param default:配置项默认值
        :return:
        """
        if default is None:
            default = []
        values = self.get_conf(key)
        if values:
            return values.split(',')
        return default

    def get_all_conf(self) -> dict:
        """
        获取所有配置数据
        :return:
        """
        all_config = {}
        all_config.update(self.__disconf)
        all_config.update(self.__configmap.get_all())
        return all_config

    def add_api(self, path: str, endpoint: Callable[..., Any], methods: Optional[Union[Set[str], List[str]]] = None):
        """
        增加服务接口，此函数需要在init_api前调用
        :param path:接口访问路径
        :param endpoint:接口实现函数
        :param methods:接口访问方式，如GET、POST等
        :return:
        """
        self.__ai_router.add_api_route(path, endpoint, methods=methods)

    def add_subscribe(self, call_back, topic=None):
        """
        :param call_back:回调函数
        :param topic:订阅主题
        """
        self.__mq_handler.add_subscribe(call_back, topic)

    def download_models(self, file_names, retry=2):
        """
        下载文件
        :param file_names:模型文件名列表
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :return: 模型目录路径
        """
        local_model_dir = "/mnt/models"
        os.makedirs(local_model_dir, exist_ok=True)
        for file_name in file_names:
            file_path = local_model_dir + '/' + file_name
            if os.path.exists(file_path):
                continue
            self.__client.download_s3_file(file_name, file_path, retry)
        return local_model_dir

    async def download_file(self, file_url, retry=2, timeout=None):
        """
        下载文件
        :param timeout:
        :param file_url:文件地址
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 文件下载超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:文件数据字节数组
        """
        return await self.__client.download_file(file_url=file_url, retry=retry, timeout=timeout)

    def download_file_sync(self, file_url, retry=2, timeout=None):
        """
        下载文件(同步)
        :param timeout:
        :param file_url:文件地址
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 文件下载超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:文件数据字节数组
        """
        return self.__client.download_file_sync(file_url=file_url, retry=retry, timeout=timeout)

    async def upload_file(self, file_path: str, retry=2) -> str:
        """
        :param file_path:本地文件路径
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.upload_file_sync(file_path, retry)

    def upload_file_sync(self, file_path: str, retry=2) -> str:
        """
        :param file_path:本地文件路径
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.__client.upload_file(file_path, retry)

    async def upload_file_from_buffer(self, file_extension: str, body, retry=2) -> str:
        """
        :param file_extension: 文件扩展名，如.txt|.png
        :param body: 文件流,必须实现了read方法
        :param retry: 失败重试次数,默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.upload_file_sync_from_buffer(file_extension, body, retry)

    def upload_file_sync_from_buffer(self, file_extension: str, body, retry=2) -> str:
        """
        :param file_extension: 文件扩展名，如.txt|.png
        :param body: 文件流,必须实现了read方法
        :param retry: 失败重试次数,默认为2次，建议不大于3次
        :return: 文件url
        """
        return self.__client.upload_file_from_buffer(file_extension, body, retry)

    async def send_mq_msg(self, body, topic=None, keys=None, tags=None):
        """
        :param body: rocketMQ消息内容
        :param topic: rocketMQ消息主题，非必传，未配置默认主题时必传
        :param keys: rocketMQ消息唯一标识，非必传
        :param tags: rocketMQ消息标签，非必传
        """
        self.__mq_handler.send_sync(body, topic, keys, tags)

    def send_mq_msg_sync(self, body, topic=None, keys=None, tags=None):
        """
        :param body: rocketMQ消息内容
        :param topic: rocketMQ消息主题，非必传，未配置默认主题时必传
        :param keys: rocketMQ消息唯一标识，非必传
        :param tags: rocketMQ消息标签，非必传
        """
        self.__mq_handler.send_sync(body, topic, keys, tags)

    async def call_back(self, url: str, body: dict, retry=2, timeout=None):
        """
        推理结果回调
        :param url:回调地址
        :param body:回调内容，字典中必须包含‘uuid’的key，且value符合UUID规则
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 回调超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:回调请求响应体
        """
        if not re.match(r'[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}', body.get('uuid', '')):
            raise Exception('The request body of call back must contain the correct UUID.')
        return await self.__client.call_back(url, body, retry, timeout)

    def call_back_sync(self, url: str, body: dict, retry=2, timeout=None):
        """
        推理结果回调
        :param url:回调地址
        :param body:回调内容，字典中必须包含‘uuid’的key，且value符合UUID规则
        :param retry:失败重试次数，默认为2次，建议不大于3次
        :param timeout: 回调超时时间（秒），默认为配置文件ai-commons.properties中http.timeout，目前为15秒
        :return:回调请求响应体
        """
        if not re.match(r'[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}', body.get('uuid', '')):
            raise Exception('The request body of call back must contain the correct UUID.')
        return self.__client.call_back_sync(url, body, retry, timeout)


class Interceptor(BaseHTTPMiddleware):
    """
    拦截所有请求
    """

    async def dispatch(self, request: HttpRequest, call_next: RequestResponseEndpoint) -> HttpResponse:
        # 生成请求标识
        app_id.set(request.query_params.get('appId'))
        request_id.set(utils.tid_maker())
        # 记录客户端请求的URL，包括未定义的URL，
        # 拦截器中不能获取request中body内容，会导致请求阻塞
        logger = plogger if request.scope['path'] == '/time' else klogger
        logger.info('Request URL: {} {}'.format(request.method, request.url))
        response = await call_next(request)
        logger.info('Response HTTP Status Code: {}'.format(response.status_code))
        return response


def probe(q: Optional[str] = None):
    """k8s 探针 http监控服务请求地址"""
    result = {'code': 0,
              'msg': 'success',
              'data': {
                  'time': time.strftime('%Y-%m-%d-%H-%M', time.localtime())
              }}
    if q:
        result['data']['q'] = q
    return result


async def api_exception_handler(request: Request, exc: ApiException) -> ORJSONResponse:
    """拦截接口抛出的所有自定义的HTTPException 异常"""
    klogger.exception('Request Exception:'.format())
    response = ORJSONResponse({
        "code": exc.error_code,
        "msg": exc.msg,
        "data": exc.data
    }, status_code=exc.status_code)
    klogger.info('Response Content:{}'.format(response.body.decode('utf-8')))
    klogger.info('Response HTTP Status Code: {}'.format(response.status_code))
    return response


async def app_exception(request: Request, exc: Exception) -> ORJSONResponse:
    """拦截接口抛出的所有未知非HTTPException 异常"""
    klogger.exception('Request Exception:'.format())
    response = ORJSONResponse({
        "code": 10024,
        "msg": 'Unknown error',
        "data": {},
    }, status_code=500)
    klogger.info('Response Content:{}'.format(response.body.decode('utf-8')))
    klogger.info('Response HTTP Status Code: {}'.format(response.status_code))
    return response
