#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""func_compile.py

语法：compile(source, filename, mode[, flags[, dont_inherit]])
source -- 字符串或者AST（Abstract Syntax Trees）对象
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值
mode -- 指定编译代码的种类。可以指定为 exec, eval, single
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象
flags和dont_inherit是用来控制编译源码时的标志"""

str_code = 'for i in range(10): print(i, end=" ")'
exec_code = compile(str_code, '', 'exec')
exec(exec_code)

print()

str_code = 'print("hello, world!")'
single_code = compile(str_code, '', 'single')
exec(single_code)

str_code = '[1, 2, 3, 4, 5]'
eval_code = compile(str_code, '', 'eval')
print(eval(eval_code))

