#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_delattr.py
删除属性"""

class MyClass(object): pass

mc = MyClass()
mc.name = 'mc name'
print(mc.name)

delattr(mc, 'name')
print(hasattr(mc, 'name'))
