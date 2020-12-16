# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
from environs import Env

env = Env()
env.read_env("./.env")

DEBUG = env.bool('DEBUG', default=False)

bind = '0.0.0.0:5005'
workers = 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
if DEBUG:
    reload = True
