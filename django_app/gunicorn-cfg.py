# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""
import os

RELOAD = os.environ.get("DEBUG", "False")

bind = "0.0.0.0:5005"
workers = 1
accesslog = "-"
loglevel = "debug"
capture_output = True
enable_stdio_inheritance = True
if RELOAD == "True":
    reload = True
    print("Reload for GUnicorn is active")
