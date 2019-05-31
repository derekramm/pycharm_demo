#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_isinstance.py
判断一个对象是否是一个已知的类型，类似 type()
isinstance() 与 type() 区别：
type() 不会认为子类是一种父类类型，不考虑继承关系
isinstance() 会认为子类是一种父类类型，考虑继承关系
如果要判断两个类型是否相同推荐使用 isinstance()"""

gender = True
print(f'{isinstance(gender, bool)}')
print(f'{isinstance(gender, int)}')
