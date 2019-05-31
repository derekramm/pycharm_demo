#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_iter.py
用来生成迭代器"""

nums = iter(range(3))
print(nums)

for n in nums: print(n, end=',')
