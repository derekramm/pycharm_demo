#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_bytearray.py
返回字节数组，要求每个元素的值范围是 0<=x<256

如果 source 为整数，则返回一个长度为 source 的初始化数组
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray
如果没有输入任何参数，默认就是初始化数组为0个元素。"""

print(bytearray())
print(bytearray(18))
print(bytearray('derek', encoding='utf-8'))
print(bytearray([1, 2, 3]))
