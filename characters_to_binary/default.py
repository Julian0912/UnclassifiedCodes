# -*- coding:utf8 -*-
# Author: Julian Black
# Function:
#
import re


def __judge_except_one_zero(p: str):
    p = p.replace("1", "")
    p = p.replace("0", "")
    if p:
        return False
    else:
        return True


def __whether_has_alpha(l:list):
    l.pop(0)
    for i in l:
        if len(i) != 2:
            return False
    else:
        return True


def b_c(b: str) -> str:
    if not __judge_except_one_zero(b):
        raise Exception("错误：包含非0和1字符！")
    h = hex(int(b, 2))[2:]
    hl = re.findall(".{2}", h)
    hl.insert(0, "")
    bs = "b'{}'".format("\\x".join(hl))
    c = eval(bs).decode("gbk")
    return c


def c_b(c: str) -> str:
    b = c.encode("gbk")
    bs = str(b)[2:-1]
    bl = bs.split("\\x")
    # if not __whether_has_alpha(bl):
    #     raise Exception("错误：包含非中文字符！")
    hs = "".join(bl)
    b = bin(int(hs, 16))[2:]
    return b
