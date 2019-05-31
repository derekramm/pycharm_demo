#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_eval.py
执行一个字符串表达式，并返回表达式的值
语法：eval(expression[, globals[, locals]])
expression -- 表达式
globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象
locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象"""

number = 18
print(f'{number} * 2 = {eval("number * 2")}')

names = eval('["ramm", "derek"]')
print(type(names), names)

print(eval('__import__("sys").path'))  # 危险的注入
print(eval('__import__("os").system("ls")'))  # 危险的注入
