#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_repr.py
将对象转化为供解释器读取的形式"""

class MyClass(object):
    def __str__(self): return 'this is MyClass'
    def __repr__(self): return 'MyClass()'

print(MyClass())
print(repr(MyClass()))
print(eval(repr(MyClass())))