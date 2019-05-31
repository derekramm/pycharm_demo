#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_exec.py
执行储存在字符串或文件中的Python语句"""

exec('print("hello, world!")')
exec('''for i in range(3):
    print(f'{i}: hello, world!')''')
