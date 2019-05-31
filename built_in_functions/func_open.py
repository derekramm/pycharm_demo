#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_open.py
用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写"""

with open('readme.md', 'r+') as f:
    print(f.read())

with open('readme.md', 'rb+') as f:
    print(f.read())