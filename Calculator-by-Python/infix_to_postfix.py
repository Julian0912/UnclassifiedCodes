# -*- coding:utf8 -*-
# Author: Julian Black
# Function: Convert nifix expression to postfix expression
#
import my_stack


class InfixToPostfix(object):
    def __init__(self, expr: str):
        self.__expr_list = list()
        self.__str_to_list(expr)
        self.__result = str()
        self.__stack = my_stack.MyStack()  # 这个栈用来储存符号
        self.__main_convert()

    def __str_to_list(self,expr:str):
        """将字符分隔成列表"""
        for i in expr:
            if not self.__expr_list:
                self.__expr_list.append(i)
            elif i.isdecimal() and self.__expr_list[-1].isdecimal():
                self.__expr_list[-1] += i
            else:
                self.__expr_list.append(i)

    def __judge_priority(self, s):
        m_d = ["*", "/"]
        a_m = ["+", "-"]
        if s == "(":
            self.__stack.push(s)
        elif s == ")":
            j = self.__stack.get_top()
            while j != "(":
                self.__result += self.__stack.pop() + " "
                j = self.__stack.get_top()
            self.__stack.pop()
        elif s in a_m:
            j = self.__stack.get_top()
            while j != "(" and j is not None:
                self.__result += self.__stack.pop() + " "
                j = self.__stack.get_top()
            self.__stack.push(s)
        elif s in m_d:
            j = self.__stack.get_top()
            while j != "(" and j not in a_m and j is not None:
                self.__result += self.__stack.pop() + " "
                j = self.__stack.get_top()
            self.__stack.push(s)

    def __main_convert(self):
        for i in self.__expr_list:
            if i.isdecimal():
                self.__result += i + " "
            elif self.__stack.get_len() == 0:
                self.__stack.push(i)
            else:
                self.__judge_priority(i)
        # 把剩余在栈里的元素弹出来
        while self.__stack.get_len() != 0:
            self.__result += self.__stack.pop()+" "

    def get_expr(self):
        return self.__result
