# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)

bind = '0.0.0.0:5005'
workers = 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
if DEBUG:
    reload = True
