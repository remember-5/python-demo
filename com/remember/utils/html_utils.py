# -*- coding: utf-8 -*-
import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from com.remember.utils.string_utils import StringUtils


class HtmlUtils:

    @staticmethod
    def get(url):
        """
        根据url获取html代码
        :param url: 需要爬取的地址
        :return: bs4格式的html
        """
        # 请求头
        header = {
            'User-Agent':
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.87 '
                'Safari/537.36',
        }
        response = requests.get(url=url, headers=header)
        # 判定是否访问成功
        if response.status_code != 200:
            return None
        # 设置编码
        response.encoding = "UTF-8"
        return BeautifulSoup(response.text, 'html.parser')

    @staticmethod
    def time_roll_html(url, roll_time=10):
        """
        滚动加载页面 最多获取到（0,100000）的长度
        :param url: 需要爬取的地址
        :param roll_time: 滚动时间，默认10秒
        :return: bs4格式的html
        """
        driver = webdriver.Chrome()
        driver.get(url)
        for i in range(0, roll_time):
            driver.execute_script("window.scrollBy(0,100000)")
            time.sleep(1)
        bf = driver.page_source
        driver.close()
        return BeautifulSoup(bf, 'html.parser')

    @staticmethod
    def roll_html(url, roll_time=10):
        """
        滚动加载页面 无限获取长度
        :param url: 需要爬取的地址
        :param roll_time:滚动时间，默认10秒
        :return:bs4格式的html
        """
        # 创建浏览器
        driver = webdriver.Chrome()
        # 获取url
        driver.get(url)
        for i in range(0, roll_time):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight); "
                                  "var lenOfPage=document.body.scrollHeight; return lenOfPage;")
            time.sleep(1)
        # 获取页面html
        bf = driver.page_source
        driver.close()
        return BeautifulSoup(bf, 'html.parser')

    @staticmethod
    def get_url_param(url):
        """
        获取url中的参数
        :param url:url
        :return:参数json
        """
        # 如果为None及为空
        if url is None:
            return None
        # 截取url、和参数
        _all = url.split('?')
        if len(_all) < 2:
            return None
        # 获取url
        # url = _all[0]
        # 所有参数字符串
        params_str = _all[1]
        # 分割所有参数字符串 结果 ['key=value','key1=key2'...]
        params = params_str.split('&')
        # 结果集
        result = {}
        for param in iter(params):
            # 判断'='第一次出现的位置
            split_num = StringUtils.index_of_str(param, '=')
            # 添加至结果集 {key1:value1,key2:value2...}
            result[param[0:split_num]] = param[split_num + 1:]
        return result

# if __name__ == '__main__':
#     result = HtmlUtils.get_url_param('http://mp.sohu.com/profile?'
#                                      'xpt=OTgwNTcyNjY1REQ5MEE3MkU0MTYyRDFERTM3NURCRDdAcXEuc29odS5jb20='
#                                      '&wangjiahao=wang===&name=zhli')
#     print(result)
