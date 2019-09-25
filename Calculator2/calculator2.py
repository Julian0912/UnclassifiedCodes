# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 用后序表达式实现计算器
#


class EmptyError(Exception):
    """专门为对空栈进行弹出或查询操作时设计的异常"""
    pass


class UnknownError(Exception):
    """未知异常"""
    pass


class Stack(object):
    """实现一个栈"""

    def __init__(self):
        self.stack = []
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self.stack.append(e)
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        e = self.stack.pop()
        self.size -= 1
        return e

    def peek(self):
        if self.is_empty():
            raise EmptyError('stack is empty')
        return self.stack[-1]


class Calculator(object):
    """计算器，暂不支持负数和小数运算

    异常信息通常反映在栈上，不能正确处理
    """

    def __init__(self, expr: str):
        """初始化计算器

        expr：中序算数表达式
        """
        self.expr = expr

    def __arrange_format(self):
        """整理表达式，在操作数和运算符分开；不做语法检查

        :return: List[str]
        """
        expr_list = []  # 用于存储分割开的表达式元素
        operators = '+-*/()'
        operands = '0123456789'
        temp_num = ''  # 用于缓存两位以上的数字
        for e in self.expr:
            if e.isspace():  # 如果是空格，直接略过
                continue
            if e in operators:  # 如果是运算符，
                if temp_num:  # 加入运算符之前存在缓存数字，先加入数字，再加入运算符，
                    expr_list.append(temp_num)
                    temp_num = ''  # 同时清空缓存
                expr_list.append(e)
            elif e in operands:  # 如果是数字，加入缓存
                temp_num += e
            else:
                raise UnknownError('there might be invalid characters in the expression')
        if temp_num:  # 操作完成后，将最后一个缓存的数字加入列表
            expr_list.append(temp_num)
        return expr_list

    def __infix_to_postfix(self):
        """把中序表达式转变为后序表达式，并返回列表形式的后序表达式

        :return: List[str]
        """
        m_d = '*/'
        a_s = '+-'  # 为判断优先级做准备
        postfix_list = []  # 存储最终中序表达式结果的列表
        op_stack = Stack()  # 转换栈，存储运算符
        for e in self.__arrange_format():
            if e == '(':  # 如果是左括号，直接压入栈
                op_stack.push(e)
            elif e == ')':  # 如果是右括号，则把栈内第一个左括号之前的运算符都弹出
                while op_stack.peek() != '(':
                    postfix_list.append(op_stack.pop())  # 并添加到列表
                op_stack.pop()  # 弹出左括号
            elif e in m_d:  # 如果是乘除
                while (not op_stack.is_empty()) and (op_stack.peek() in m_d):  # 栈非空且栈顶是乘除
                    postfix_list.append(op_stack.pop())  # 把所有乘除弹出
                op_stack.push(e)  # 把当前元素压入
            elif e in a_s:  # 如果是加减
                while (not op_stack.is_empty()) and (op_stack.peek() in m_d+a_s):  # 栈非空且栈顶是加减乘除
                    postfix_list.append(op_stack.pop())  # 把所有加减乘除弹出
                op_stack.push(e)  # 把当前元素压入
            elif e.isdigit():  # 如果是数字，直接加入列表
                postfix_list.append(e)
            else:
                raise UnknownError('there might be invalid characters in the expression')
        while not op_stack.is_empty():
            postfix_list.append(op_stack.pop())  # 把剩余元素加入列表
        return postfix_list

    def calculate(self):
        """计算器类的主方法"""
        cal_stack = Stack()  # 计算栈
        operators = '+-*/'
        for e in self.__infix_to_postfix():
            if e.isdigit():  # 如果是数字，直接压入
                cal_stack.push(e)
            elif e in operators:  # 如果是运算符
                after = cal_stack.pop()  # 后一个数字
                before = cal_stack.pop()  # 前一个数字
                res = eval(before+e+after)  # 结果
                cal_stack.push(str(res))  # 把新结果压入栈
            else:
                raise UnknownError('there might be invalid characters in the expression')
        result = cal_stack.pop()  # 弹出最终结果
        if not cal_stack.is_empty():  # 正常情况下栈里只剩最后的最终结果
            raise UnknownError('unknown error')
        return result


if __name__ == '__main__':
    expression = input('输入中序算数表达式：')
    c = Calculator(expression)
    print(c.calculate())


