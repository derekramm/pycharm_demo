#!/usr/bin/env python
# -*- coding:UTF-8 -*-
"""
dongxiaoyong
2018/5/19
single_heart.py
"""
import turtle  # 绘图模板
import random  # 随机数模板

t = turtle.Turtle()  # 创建绘图对象
t.screen.screensize(800, 800, 'Pink')  # 设置大小和背景色

t.speed(1000)  # 设置绘制速度
colors = '0123456789abcdef'  # 设置随机取色样本


def move_pen(x, y):
    """移动画笔"""
    t.up()  # 提起画笔(表示此时不在画板上绘图)
    t.goto(x, y)  # 移动到指定位置, (0,0) 代表画布正中央
    t.down()  # 放下画笔(此时会在画布上绘制)


def draw_heart(size, start_degree=0, isfill=False):
    """绘制心形
    参数列表:
    size: 心形的大小
    start_degree: 心形的角度, 0 代表垂直
    isfill: 是否填充心形"""

    t.setheading(start_degree)  # 设定初始角度

    if isfill:
        t.begin_fill()  # 填充绘制

    # 无论是否填充,都需要描边绘制
    t.left(45)  # 绘制方向 逆时针旋转45度
    t.fd(size)  # 按照指定方向向前绘制 size 大小的直线
    t.circle(size // 2, 180)  # 绘制180度(半圆)的弧形
    t.right(90)  # 绘制方向 顺时针旋转90度
    t.circle(size // 2, 180)  # 绘制180度(半圆)的弧形
    t.fd(size)  # 按照指定方向向前绘制 size 大小的直线

    if isfill:
        t.end_fill()  # 结束填充


def random_pen():
    """定义随机画笔"""
    pen_size = random.randint(1, 10)  # 画笔粗细随机 (1-10)
    heart_size = random.randint(10, t.screen.window_width() // 6)  # 心形大小随机 (10 - 画布 1/4 宽度)
    line_color = '#{}'.format(''.join(random.sample(colors, 6)))  # 线条颜色随机
    fill_color = '#{}'.format(''.join(random.sample(colors, 6)))  # 填充颜色随机

    t.pensize(pen_size)  # 设置画笔粗细
    t.color(line_color, fill_color)  # 设置画笔线条颜色和填充颜色
    return pen_size, heart_size, line_color, fill_color  # 返回画笔参数


def main():
    """主函数绘制"""
    # s = input(r'请输入对方的名字和想说的话, 换行用 @@ 区分:')
    s = "520情人节快乐@@达内直播课@@兴趣驱动学习@@让学习成为一种习惯!@@TLV_CN"
    lines = s.split('@@')

    # heart_num = int(input('请输入开场出现的心形数量(最好是对方的年龄):'))
    heart_num = 20

    # uname = input('请输入你的名字: ')
    uname = "TEDU LIVE VIDEO"

    for i in range(heart_num):
        size = random_pen()[1]  # 重置随机画笔, 获取心形大小
        # 随机移动画笔到画布的某个位置, 作为绘制心形的起始位置
        move_pen(
            random.randint(-t.screen.window_width() // 2, t.screen.window_height() // 2),  # 水平位置
            random.randint(-t.screen.window_width() // 2, t.screen.window_height() // 2)  # 垂直位置
        )
        draw_heart(size, random.randint(0, 360))  # 绘制心形(不填充)

    t.speed(3)  # 放慢绘制速度
    # t.clear()  # 是否清空之前的画布
    t.screen.screensize(800, 600, 'pink')  # 设置画布大小和背景色

    move_pen(0, -t.screen.window_height() // 4)  # 移动画笔到画布中央正下方
    t.pensize(40)  # 重新设定画笔粗细
    t.color('red', 'red')  # 设定画笔颜色为红色(貌似也不敢选别的颜色)
    draw_heart(t.screen.window_width() // 3, isfill=True)  # 绘制心形( 大小为画布大小的 1/3, 并填充)

    t.pensize(6)  # 设置画笔粗细, 用来写文本
    move_pen(-len(s) // 2 * 24, len(lines) * 24)  # 根据文本长度, 移动画笔, 尽量保证文字在心形正中央
    t.color('white')  # 设置文字颜色

    for index, line in enumerate(lines):
        move_pen(0, (len(lines) // 2 - index) * 54)
        t.write(line, move=False, font=("微软雅黑", 32, "normal"), align='center')  # 在心形中绘制文字

    t.pensize(8)  # 设置画笔粗细, 用来写文本
    move_pen(t.screen.window_width() // 6.5, -t.screen.window_height() // 6.5)  # 画笔移动到右下角
    t.color('red')  # 设置画笔颜色
    t.write(uname, move=True, font=("微软雅黑", 32, "normal"))

    turtle.done()  # 绘制完成, 保留窗口


if __name__ == '__main__':
    main()
