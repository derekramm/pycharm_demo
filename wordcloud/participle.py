# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 21:28:56 2017

@author: xu
"""
# 加载模块
import codecs
from os import path
import jieba

# 使用jieba分词
def save_jieba_result():
    # 设置多线程切割
    # jieba.enable_parallel(4)
    # 读取评论文本
    dirs = path.join(path.dirname(__file__), './comment.txt')
    print(dirs)
    with codecs.open(dirs, encoding='utf-8') as f:
        comment_text = f.read()

    # 将jieba分词得到的关键词用空格连接成为字符串
    cut_text = " ".join(jieba.cut(comment_text))
    with codecs.open('jieba_result.txt', 'a', encoding='utf-8') as f:
        f.write(cut_text)

if __name__ == "__main__":
    # 调用jieba分词
    save_jieba_result()
