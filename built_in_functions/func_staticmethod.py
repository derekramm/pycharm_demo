#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_staticmethod.py
返回函数的静态方法"""

class MyClass(object):
    @staticmethod
    def show(): print('this is MyClass')

MyClass.show()
MyClass().show()