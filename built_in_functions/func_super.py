#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_super.py
用于调用父类(超类)的一个方法
语法：super(type[, object-or-type])
type -- 类。
object-or-type -- 类，一般是 self
Python3.x 和 Python2.x 的一个区别是
Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx"""

class Pet(object):
    def show(self): return 'my name is '

class Cat(Pet):
    def show(self): return super().show() + 'cat'

print(Pet().show())
print(Cat().show())