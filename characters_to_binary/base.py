# -*- coding:utf8 -*-
# Author: Julian Black
# Function: 
#
from default import b_c,c_b


while True:
    choice = input("二进制转汉字扣1，汉字转二进制扣2，退出扣0：")
    if choice == "0":
        break
    elif choice == "1":
        try:
            binary = input("请输入01字符串：")
            if binary == "q":
                continue
            char = b_c(binary)
        except UnicodeDecodeError:
            print("错误：存在不能解码的字符，请重新检查密文！")
        except Exception as e:
            print(e)
        else:
            print("解码成功！")
            print("明文："+char)
    elif choice == "2":
        try:
            character = input("请输入汉字：")
            if character == "q":
                continue
            bina = c_b(character)
        except Exception as e:
            print(e)
        else:
            print("编译成功！")
            print("密文："+bina)
    else:
        print("没有该命令！")





