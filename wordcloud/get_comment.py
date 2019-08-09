# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:44:16 2017

@author: changjin
"""
import requests
import random
import time
from bs4 import BeautifulSoup
import codecs


def download_page(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
    html = requests.get(url, headers=header).content
    return html


def get_douban_comments(res):
    # 评论列表
    comments_list = []
    # 使用BeautifulSoup解析Html
    soup = BeautifulSoup(res)
    # 获取对应评论标签的内容
    comment_nodes = soup.select('.comment > p')
    # 将评论内容逐条添加进评论列表
    for node in comment_nodes:
        comments_list.append(node.get_text().strip().replace("\n", "") + u'\n')
    return comments_list


# 主函数入口
if __name__ == '__main__':

    # 豆瓣评论页地址
    templateurl = 'https://movie.douban.com/subject/26363254/comments?start={}&limit=20&sort=new_score&status=P'
    # 开始爬取
    with codecs.open('comment.txt', 'a', encoding='utf-8') as f:
        # 5000*20共计十万条
        for i in range(1000):
            print ('开始爬取%d页评论...'%(i))
            targeturl = templateurl.format(i * 20)
            res = download_page(targeturl)

            f.writelines(get_douban_comments(res))
            # 设置爬虫工作间隔时间
            time.sleep(1 + float(random.randint(1, 20)) / 20)
