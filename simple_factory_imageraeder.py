#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""simple_factory_imageraeder.py
通过简单工厂实现不同方式的图片读取"""

from abc import ABCMeta, abstractmethod


class ImageReader(object, metaclass=ABCMeta):
    @abstractmethod
    def read(self, fp): pass  # 读取图片


class PilReader(ImageReader):
    def read(self, fp):
        from PIL import Image  # 用于读写图片
        im = Image.open(fp)  # 根据路径读取图片
        im.show()  # 显式图片
        print('read by pil:', im.format, im.size)  # 输出图片格式和大小


class SkimageReader(ImageReader):
    def read(self, fp):
        from skimage import io
        im = io.imread(fp)  # 根据路径读取图片
        io.imshow(im)  # 将图片加载到面板
        io.show()  # 显式面板
        print('read by skimage:', im.shape, im.size)


class MatplotlibReader(ImageReader):
    def read(self, fp):
        import matplotlib.pyplot as plt  # 用于显示图片
        import matplotlib.image as mpimg  # 用于读取图片
        im = mpimg.imread(fp)  # 根据路径读取图片
        plt.imshow(im)  # 将图片加载到面板
        plt.show()  # 显示面板
        print('read by matplotlib:', im.shape, im.size)  # 输出图片的形状和大小


class ImageReaderFactory(object):
    @staticmethod
    def get_reader(r_name):
        # 第01步：补全工厂中的代码
        raise NotImplementedError


if __name__ == '__main__':
    file_path = input('请输入图片地址：')  # 这里需要你复制一张图片到同级目录
    reader_name = input('请输入处理方式（pil | skimage | matplotlib）：')
    # 第02步： 调用工厂
