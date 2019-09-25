# -*- coding:utf8 -*-
# Author: Julian Black
# Function: The Main Function of the Calculation
#
import infix_to_postfix
import calc_by_postfix


class Calculate(object):
    def __init__(self, expr):
        self.expr = expr

    def __main(self):
        np = infix_to_postfix.InfixToPostfix(self.expr)
        cp = calc_by_postfix.Calculation(np.get_expr())
        return cp.get_result()

    def __str__(self):
        return self.__main()
