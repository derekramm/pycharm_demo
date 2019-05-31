#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_memoryview.py
返回给定参数的内存查看对象"""

b = bytearray('derek', encoding='utf-8')
print(b)
mv = memoryview(b)
print(mv)
for i in mv:
    print(i)
