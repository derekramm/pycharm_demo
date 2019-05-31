#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_import.py
动态加载类和函数"""

print(eval("__import__('datetime').date.today()"))
print(eval("__import__('time').asctime()"))
