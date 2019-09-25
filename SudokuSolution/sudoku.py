# -*- coding:utf8 -*-
# Author: Julian Black
# Description: 给定数独，求得其解
#


def update_potential(s_ls: list, v_dic: dict, n: int, pot: set, xy: int):
    """更新数独表中空位的可能值

    :param s_ls: sudoku_list 二维列表
    :param v_dic: vacancy字典
    :param n: 行号、列号
    :param pot: 可能值集合
    :param xy: 在处理行时取0，处理列时取1
    """
    to_del_key = []  # vacancy里待删除的单元格
    for key_tup in v_dic.keys():
        if key_tup[xy] == n:  # 找到当前行/列的空位
            if len(v_dic[key_tup]) == 0:
                v_dic[key_tup] = pot
            else:
                new_set = v_dic[key_tup] & pot
                v_dic[key_tup] = new_set
            if len(v_dic[key_tup]) == 1:  # 如果可能值只剩一个，则填
                s_ls[key_tup[0]][key_tup[1]] = v_dic[key_tup].pop()
                to_del_key.append(key_tup)
    for key in to_del_key:
        v_dic.pop(key)  # 删除已填的单元格


def manage_row(s_ls: list, v_dic: dict):
    """处理行

    :param s_ls: sudoku_list二维列表
    :param v_dic: vacancy字典
    """
    for row_x in s_ls:
        num_temp = set('123456789')  # 可能值，每计算一行都重新计数
        r = s_ls.index(row_x)  # 行号
        cl = 0  # 单元格计数
        for cell in row_x:
            if cell == '?':
                pos = r, cl  # 找到当前单元格的位置
                v_dic.setdefault(pos, set())  # 如果位置不存在，加入空集合，如果存在，不做操作
            elif cell in num_temp:
                num_temp.discard(cell)  # 在可能值里删除已存在的值
            else:
                raise ValueError("第{}行有未知符号！".format(r + 1))
            cl += 1
        # 去掉已存在的值后，添加空位的可能值
        # 如果空位已存在可能值，取交集
        update_potential(s_ls, v_dic, r, num_temp, 0)


def manage_col(s_ls: list, v_dic: dict):
    """处理列

    :param s_ls: sudoku_list
    :param v_dic: vacancy
    """
    col_sets = {k: set('123456789') for k in range(9)}  # 每一列对应一组可能值
    for row_y in s_ls:
        r = s_ls.index(row_y)
        cl = 0
        for cell in row_y:
            if cell == '?':
                pos = r, cl
                v_dic.setdefault(pos, set())
            elif cell in col_sets[cl]:
                col_sets[cl].discard(cell)
            else:
                raise ValueError("第{}行有未知符号！".format(r + 1))
            cl += 1
    for r in range(9):
        update_potential(s_ls, v_dic, r, col_sets[r], 1)


def manage_pal(s_ls: list, v_dic: dict):
    """处理宫

    :param s_ls: sudoku_list
    :param v_dic: vacancy
    """
    pal_sets = {(r, c): set('123456789') for r in range(3) for c in range(3)}
    for row_p in s_ls:
        r = s_ls.index(row_p)
        cl = 0
        for cell in row_p:
            if cell == '?':
                pos = r, cl
                v_dic.setdefault(pos, set())
            elif cell in pal_sets[(r // 3, cl // 3)]:
                pal_sets[(r // 3, cl // 3)].discard(cell)
            else:
                raise ValueError("第{}行有未知符号！".format(r + 1))
            cl += 1
    # 处理宫时单独更新可能值
    pal_to_del = []  # 待删除的单元格
    for k_tup in v_dic.keys():
        k = k_tup[0] // 3, k_tup[1] // 3  # 找到所属宫的坐标
        if len(v_dic[k_tup]) == 0:
            v_dic[k_tup] = pal_sets[k]
        else:
            new_s = v_dic[k_tup] & pal_sets[k]
            v_dic[k_tup] = new_s
        if len(v_dic[k_tup]) == 1:
            s_ls[k_tup[0]][k_tup[1]] = v_dic[k_tup].pop()
            pal_to_del.append(k_tup)
    for ke in pal_to_del:
        v_dic.pop(ke)


def main(circle=100):
    """
    文本文件内容的存储方式为数字和英文问号存储，一共九行，空位用一个问号代替
    合格文件的某一行：?,6,1,?,3,?,?,2,?
    每行逗号必须有8个

    :param circle: 循环解析次数
    """
    f_name = input("请输入数独文件名（不需要后缀）：")
    sudoku_file = open(f_name + '.txt', 'r')

    print("正在读取文件...")

    sudoku_list = []
    file_data = sudoku_file.readlines()
    for line in file_data:
        trans_line = line.strip().split(',')
        sudoku_list.append(trans_line)
    # 至此，我们得到了一个用二位列表格式化的数独：sudoku_list

    """检查数独格式"""
    for row in sudoku_list:
        if len(row) != 9:
            r = sudoku_list.index(row)
            raise ValueError("第{}行格式错误！".format(r + 1))

    print("读取文件成功！")
    print("正在解析...")

    vacancy = {}  # 用于标记空位里的可能值，格式为{(0,0):{4,7,8,9}}，一旦可能值只剩一个，则可填
    # set.discard(e) 从集合中删除一个元素
    count = 0  # 计数器
    while True:
        manage_row(sudoku_list, vacancy)
        manage_col(sudoku_list, vacancy)
        manage_pal(sudoku_list, vacancy)
        if len(vacancy) == 0:
            break
        count += 1
        if count > circle:
            raise TimeoutError('超过循环解析次数，解析未成功！')

    print("解析成功！")
    print("正在写入新文件...")

    solution_file = open(f_name + '_solution.txt', 'w')
    for row in sudoku_list:
        row_res = ','.join(row) + '\n'
        solution_file.write(row_res)
    solution_file.close()
    sudoku_file.close()

    print("写入成功！")


if __name__ == '__main__':
    main()
