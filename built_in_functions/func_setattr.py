#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_setattr.py
属性赋值"""

class MyClass(object): pass

mc = MyClass()
setattr(mc, 'name', 'derek')
print(getattr(mc, 'name'))
