#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_any.py
判断可迭代对象中的所有元素是否有一个为True"""

flags00 = []
flags01 = [1, 1, 1]
flags02 = [1, 0, 1]
flags03 = [0, 0, 0]

print(f'any({flags00}) 的结果是 {any(flags00)}')  # 注意空列表的返回值为False
print(f'any({flags01}) 的结果是 {any(flags01)}')
print(f'any({flags02}) 的结果是 {any(flags02)}')
print(f'any({flags03}) 的结果是 {any(flags03)}')
