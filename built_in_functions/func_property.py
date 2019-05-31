#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_property.py
在新式类中返回属性值"""

class MyClass(object):
    def __init__(self):
        self._name = None
    def getname(self): return self._name
    def setname(self, value): self._name = value
    def delname(self): del self._name
    name = property(getname, setname, delname, 'name is MyClass property')

mc = MyClass()
mc.name = 'derek'
print(mc.name)
del mc.name
print(mc.name)