#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_getattr.py
用于返回一个对象属性值"""

class MyClass(object):
    name, age = 'derek', 18

mc = MyClass()
print(getattr(mc, 'name'))
print(getattr(mc, 'age'))
