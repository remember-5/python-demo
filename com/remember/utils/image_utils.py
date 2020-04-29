# -*- coding: utf-8 -*-
import urllib
import requests
from io import BytesIO
from PIL import Image


class ImageUtils:

    @staticmethod
    def web_image_prop(path):
        """
        获取网络图片的属性
        :param path:网络图片地址
        :return:图片的属性
        """
        response = requests.get(path)
        tmp_img = BytesIO(response.content)
        im = Image.open(tmp_img)
        return im
        # w = im.size[0]
        # h = im.size[1]
        # print("宽度：%s" % (w))
        # print("高度：%s" % (h))

    @staticmethod
    def web_image_width(path):
        """
        获取网络图片的宽
        :param path:网络图片地址
        :return:图片的宽
        """
        response = requests.get(path)
        tmp_img = BytesIO(response.content)
        im = Image.open(tmp_img)
        return im.size[0]

    @staticmethod
    def web_image_height(path):
        """
        获取网络图片的高
        :param path:网络图片地址
        :return:图片的高
        """
        response = requests.get(path)
        tmp_img = BytesIO(response.content)
        im = Image.open(tmp_img)
        return im.size[1]

    @staticmethod
    def save_web_image(image_url, save_path):
        """
        保存网络图片到本地
        :param image_url: 网络图片地址
        :param save_path: 保存路径
        :return: None
        """
        urllib.request.urlretrieve(image_url, save_path)
