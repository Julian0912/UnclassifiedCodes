# -*- coding:utf8 -*-
# Author: Julian Black
# Function: figure out the Tower of Hanoi
#


def get_emp_pos(start, stop):
    choices = ["A", "B", "C"]
    if start not in choices or stop not in choices:
        raise Exception(
            "There is no such position as {} or {}".format(
                start, stop))
    for i in choices:
        if i != start and i != stop:
            return i


def deal_hanoi(n: int, start="A", stop="C"):
    global i
    if n < 1:
        raise Exception("The level must larger than or equal 1")
    if n == 1:
        print("{}-->{}".format(start, stop))
        i += 1
        return
    else:
        pos = get_emp_pos(start, stop)
        deal_hanoi(n - 1, start, pos)  # 除了最底下一块其他的都挪到空位存着
        print("{}-->{}".format(start, stop))  # 把最底下一块挪到目标位
        i += 1
        deal_hanoi(n - 1, pos, stop)  # 把剩下的挪到目标位
        return


i = 0
deal_hanoi(6)
print(i)
