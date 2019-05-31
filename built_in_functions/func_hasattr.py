#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_hasattr.py
用于判断对象是否包含对应的属性"""

class MyClass:
    first_name, last_name = 'ramm', 'derek'

mc = MyClass()
print(hasattr(mc, 'first_name'))
print(hasattr(mc, 'last_name'))
