# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#


class Fraction(object):
    """此分数类型暂不支持负数和小数"""

    def __init__(self, top: int, bottom: int):
        self.num = top
        if bottom == 0:
            raise Exception("The denominator should not be zero")
        self.den = bottom
        self.__reduction()  # 约分

    def __str__(self):
        if self.num == 0:
            return "0"
        elif self.den == 1:
            return str(self.num)
        else:
            return "{}/{}".format(self.num, self.den)

    def __add__(self, frac):
        if self.den == frac.den == 1:
            return self.num + frac.num
        else:
            new_num = self.num * frac.den + self.den * frac.num
            new_den = self.den * frac.den
            new_f = Fraction(new_num, new_den)
            return new_f

    def __sub__(self, frac):
        if self < frac:
            raise Exception("This class doesn't support negative number yet")
        else:
            new_num = self.num * frac.den - self.den * frac.num
            new_den = self.den * frac.den
            new_f = Fraction(new_num, new_den)
            return new_f

    def __mul__(self, frac):
        new_num = self.num * frac.num
        new_den = self.den * frac.den
        new_f = Fraction(new_num, new_den)
        return new_f

    def __truediv__(self, frac):
        new_f = Fraction(frac.den, frac.num)
        res_f = self * new_f
        return res_f

    def __eq__(self, frac):
        return self.num * frac.den == frac.num * self.den

    def __lt__(self, frac):
        return self.num * frac.den < frac.num * self.den

    def __le__(self, frac):
        return self.num * frac.den <= frac.num * self.den

    @staticmethod
    def __get_gcd(m, n):
        """Euclid’s Algorithm"""
        while m % n != 0:
            old_m = m
            old_n = n
            #
            m = old_n
            n = old_m % old_n
        return n

    def __reduction(self):
        """有最大公约数就返回，没有就返回None"""
        gcd = self.__get_gcd(self.num, self.den)
        if gcd == 1:
            return None  # do nothing
        else:
            self.num //= gcd
            self.den //= gcd
            return gcd
