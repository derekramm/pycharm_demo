#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_dir.py
dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表
带参数时，返回参数的属性、方法列表
如果参数包含方法__dir__()，该方法将被调用
如果参数不包含__dir__()，该方法将最大限度地收集参数信息"""

class MyClass:
    name = None
    def func(self): pass

print(dir())
print(dir(str))
print(dir([]))
print(dir(MyClass))
