#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_type.py
type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象"""

import os
print(type('derek'))
print(type(str))
print(type(print))
print(type(os))

mc = type('MyClass', (object,), dict(name='derek', show=lambda self, n: print(n)))()
print(mc.name)
mc.show(mc.name)
