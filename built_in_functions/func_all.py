#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_all.py
判断可迭代对象中的所有元素是否都为True"""

flags00 = []
flags01 = [1, 1, 1]
flags02 = [1, 0, 1]
flags03 = [0, 0, 0]

print(f'all({flags00}) 的结果是 {all(flags00)}')  # 注意空列表的返回值为真
print(f'all({flags01}) 的结果是 {all(flags01)}')
print(f'all({flags02}) 的结果是 {all(flags02)}')
print(f'all({flags03}) 的结果是 {all(flags03)}')
