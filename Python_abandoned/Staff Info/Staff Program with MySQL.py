# -*- coding:utf-8 -*-

import pymysql,sys
from prettytable import PrettyTable

# 连接数据库
db = pymysql.connect("localhost","root","","employee")
c = db.cursor()

# 查询
def inquire():
    print("----欢迎来到查询页面----")
    info_list = ["id","name","sex","age","in_dpt","register_date"]
    for m in info_list: print(m)
    while True:
        inq_cho = input("请选择查询根据：")
        if inq_cho == "q":
            return None
        if inq_cho == "*":
            comm = "SELECT * FROM stuff;"
        else:
            inq_con = input("请输入已知内容：")
            comm = "SELECT * FROM stuff WHERE %s='%s';" % (inq_cho,inq_con)
        try:
            c.execute(comm)
            inq_data = c.fetchall()
            inq_pp = PrettyTable(["id","name","sex","age","in_dpt","register_date"])
            for i_d in inq_data:
                inq_pp.add_row(["%s" % i_d[0],"%s" % i_d[1],"%s" % i_d[2],"%s" % i_d[3],
                                "%s" % i_d[4],"%s" % i_d[5]])
            print(inq_pp)
        except Exception:
            print("输入错误！")

# 增加
def create():
    print("----欢迎来到新增页面----")
    info_list = ["name","sex","age","in_dpt","register_date"]
    new_list = []
    for tab in info_list:
        new_con = input("请输入%s:" % tab)
        new_list.append(new_con)
    comm = """INSERT INTO stuff(name,sex,age,in_dpt,register_date) 
          VALUES('%s','%s','%s','%s','%s');""" % (new_list[0],new_list[1],new_list[2],new_list[3],new_list[4])
    try:
        c.execute(comm)
        db.commit()
        print("信息录入成功！")
    except Exception as e:
        print(e)
        print("信息录入失败！")

# 删除
def delete():
    print("----欢迎来到删除页面----")
    info_list = ["id","name", "sex", "age", "in_dpt", "register_date"]
    for m in info_list: print(m)
    try:
        del_cho = input("请选择删除根据：")
        if del_cho == "q":
            return None
        del_con = input("请输入已知内容：")
        comm = "DELETE FROM stuff WHERE %s='%s';" % (del_cho,del_con)
        c.execute(comm)
        db.commit()
        print("信息删除成功！")
    except Exception as e:
        print(e)
        print("信息删除失败！")

# 修改
def update():
    print("----欢迎来到修改页面----")
    try:
        up_cho = input("被修改条的id：")
        info_list = ["name","sex","age","in_dpt","register_date"]
        for i in info_list: print(i)
        up_con = input("请选择要修改的项：")
        new_con = input("请输入新的内容：")
        comm = "UPDATE stuff SET %s='%s' WHERE id='%s'" % (up_con,new_con,up_cho)
        c.execute(comm)
        db.commit()
        print("信息修改成功！")
    except Exception as e:
        print(e)
        print("信息修改失败！")


# 界面
while True:
    print("----欢迎来到员工信息页面----")
    managed_list = ["inquire","create","delete","update"]
    mod = sys.modules["__main__"]
    for i in managed_list: print(i)
    choice = input("请选择操作内容：")
    if choice == "q":
        db.close()
        break
    if hasattr(mod,choice):
        func = getattr(mod,choice)
        func()
    else:
        print("输入错误！")
