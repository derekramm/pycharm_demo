#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_classmethod.py
classmethod 修饰符对应的函数不需要实例化，不需要 self 参数
但第一个参数需要是表示自身类的 cls 参数
可以来调用类的属性，类的方法，实例化对象等"""

class MyClass(object):
    class_name = 'MyClass'
    @classmethod
    def func(cls):
        print(cls.__name__)
        print(cls.class_name)
        print(cls())

MyClass.func()
