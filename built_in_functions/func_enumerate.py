#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_enumerate.py
将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标"""

weeks = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', ]
for i, w in enumerate(['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']):
    print(f'{weeks[i]} = {w}')
