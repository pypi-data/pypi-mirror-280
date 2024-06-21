#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'YAnho.wen'
__mtime__ = '2021/12/21'

"""
from contextvars import ContextVar

# 申明应用ID变量
app_id = ContextVar('Id of app', default="")

# 申明请求ID变量
request_id = ContextVar('Id of request', default="")
