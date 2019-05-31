#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_next.py
返回迭代器的下一个项目"""

class MyIter(object):
    def __init__(self):
        self.count = 65
    def __iter__(self):
        return self
    def __next__(self):
        if self.count >= 91:
            raise StopIteration
        else:
            c = chr(self.count)
            self.count += 1
            return c

if __name__ == '__main__':
    mi = MyIter()
    for i in mi:
        print(i, end=' ')
