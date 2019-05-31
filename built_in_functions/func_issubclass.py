#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_issubclass.py
判断参数 class 是否是类型参数 classinfo 的子类"""

class Student(object): pass

class Pet(object): pass

class Cat(Pet): pass

print(issubclass(Cat, Pet))
print(issubclass(Cat, Student))
print(issubclass(Cat, (Pet, Student)))
