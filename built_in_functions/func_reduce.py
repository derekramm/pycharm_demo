#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_reduce.py
会对参数序列中元素进行累积"""

from functools import reduce

def add(a, b): return a + b

print(reduce(add, range(5)))
