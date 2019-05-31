#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_sorted.py
对所有可迭代的对象进行排序操作"""

names = ['xiaoming', 'ramm', 'derek', 'leguan', 'tuatara']
print(sorted(names))
print(sorted(names, key=lambda n: len(n), reverse=True))
