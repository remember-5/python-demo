# -*- coding: utf-8 -*-
class StringUtils:
    #
    @staticmethod
    def find_last_index(string, find_str):
        """
        查找字符最后所在位置  不存在就返回-1  存在则返回位置
        :param string:被查找的字符串
        :param find_str:查找内容
        :return:存在的话，则返回位置，不存在返回-1
        """
        last_position = -1
        while True:
            position = string.find(find_str, last_position + 1)
            if position == -1:
                return last_position
            last_position = position

    @staticmethod
    def index_of_str(string, find_str):
        """
        查找字符第一次所在位置  不存在就返回-1  存在则返回位置
        :param string: 被查找的字符串
        :param find_str: 查找内容
        :return: 存在的话，则返回位置，不存在返回-1
        """
        n1 = len(string)
        n2 = len(find_str)
        for i in range(n1 - n2 + 1):
            if string[i:i + n2] == find_str:
                return i
        else:
            return -1
