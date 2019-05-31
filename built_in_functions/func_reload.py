#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_reload.py
用于重新载入之前载入的模块"""

from importlib import reload

from built_in_functions import my_module

reload(my_module)

