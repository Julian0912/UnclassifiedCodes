# -*- coding:utf8 -*-
# Author: Julian Black
# Function: Calculation by postfix expression
#
import my_stack


class Calculation(object):
    def __init__(self, expr: str):
        self.__expr_list = expr.split()
        self.__stack = my_stack.MyStack()
        self.__result = None

    def __main_calc(self):
        for i in self.__expr_list:
            if i.isdecimal():
                self.__stack.push(i)
            else:
                after = self.__stack.pop()
                before = self.__stack.pop()
                temp_expr = eval(before + i + after)
                self.__stack.push(str(temp_expr))
        self.__result = self.__stack.pop()

    def get_result(self):
        self.__main_calc()
        return self.__result
