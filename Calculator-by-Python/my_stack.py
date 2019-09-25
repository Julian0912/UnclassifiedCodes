# -*- coding:utf8 -*-
# Author: Julian Black
# Function: Stack
#


class MyStack(object):
    """其实明明列表更好用~"""

    def __init__(self):
        self.__stack = []
        self.__size = 0

    def get_len(self):
        return self.__size

    def get_top(self):
        if self.__size == 0:
            return None  # 为了避免可怕的重构；若此处改为报错处理，则其他文件会发生异常
        return self.__stack[-1]

    def push(self, element):
        self.__stack.append(element)
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            raise IndexError('stack is empty')
        e = self.__stack.pop()
        self.__size -= 1
        return e
