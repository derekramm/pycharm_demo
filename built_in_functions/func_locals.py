#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_locals.py
以字典类型返回当前位置的全部局部变量"""

print(locals())

def func():
    name, age = 'derek', 18
    print(locals())

func()