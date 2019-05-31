#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_callable.py
用于检查一个对象是否是可调用的"""

username = 'derek'

def myfunc(): pass

print(f'print 是否可以被调用：{callable(print)}')
print(f'myfunc 是否可以被调用：{callable(myfunc)}')
print(f'username 是否可以被调用：{callable(username)}')
