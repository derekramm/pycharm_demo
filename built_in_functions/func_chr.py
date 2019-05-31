#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_chr.py
用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符"""

for i in range(9800, 9812): print(chr(i), end=' ')
print()
for c in range(65, 91): print(chr(c), end=' ')
print()
for c in range(97, 123): print(chr(c), end=' ')