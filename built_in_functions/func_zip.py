#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_zip.py
用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表"""

print(list(zip((1, 2, 3), ['one', 'two', 'three'])))
