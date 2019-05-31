#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_vars.py"""

class MyClass(object):
    name = 'derek'
    def show(self): pass

print(vars())
print(vars(MyClass))