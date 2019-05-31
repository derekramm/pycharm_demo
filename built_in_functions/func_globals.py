#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_globals.py
会以字典类型返回当前位置的全部全局变量"""

def func():
    age = 18
    print(age)

name = 'derek'

print(globals())
