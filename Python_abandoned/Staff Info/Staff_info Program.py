def inquire():
    while True:
        info = input("information you know?>>")
        if info == "q":
            break
        else:
            age(info)
            dept(info)
            enroll(info)
def _print(msg):
    print("name=",msg[1],"; age=",msg[2])
def _count(num):
    print("all total:", num, "person(s)")
def age(info_age):
    if info_age.isdecimal() == True and int(info_age)<100:
        count =0
        for line in f:
            msg_age = eval(line)
            if int(msg_age[2])>int(info_age):
                _print(msg_age)
                count +=1
        _count(count)
        f.seek(0)
def dept(info_dept):
    if info_dept.isalpha() == True:
        count =0
        for line in f:
            msg_dept = eval(line)
            if msg_dept[4] == info_dept:
                _print(msg_dept)
                count +=1
        _count(count)
        f.seek(0)
def enroll(info_enroll):
    if info_enroll.isdecimal() == True and int(info_enroll) > 100:
        count =0
        for line in f:
            msg_enroll = eval(line)
            if info_enroll in msg_enroll[5]:
                _print(msg_enroll)
                count +=1
        _count(count)
        f.seek(0)

def create():
    list_id = []
    for line in f:
        _line = eval(line)
        list_id.append(_line[0])
    _max = max(list_id) + 1
    while True:
        phone_num = input("only phone numbers>>>")
        if phone_num == "q":
            break
        if phone_num.isdecimal() == False:
            print("ONLY phone numbers!")
        elif 10000000000 < int(phone_num) < 19999999999:
            list_msg = []
            list_msg.append(_max)
            staff_name = input("name=")
            staff_age = input("age=")
            staff_dept = input("dept=")
            staff_enroll = input("enroll dates=")
            list_msg.append(staff_name)
            list_msg.append(staff_age)
            list_msg.append(phone_num)
            list_msg.append(staff_dept)
            list_msg.append(staff_enroll)
            f.write(str(list_msg))
            f.write("\n")
            print("\033[31;1mmust quit the whole program next!!\033[0m")
            break
        else:
            print("Invalid phone number!")

def delete():
    print("\033[31;1mdelete one person once\033[0m")
    data = f.read()
    sub = "["
    staff_id = input("the id you wanna delete?>>")
    if staff_id.isdecimal() == False:
        print("Wrong number!")
    else:
        _id = int(staff_id)
        cou = data.count("[")
        num_list = []
        for i in range(cou):
            num = findStr(data,sub,i+1)
            _num = int(data[num+1:num+2])
            num_list.append(_num)
        f.seek(0)
        if _id not in num_list:
            print("id not found!")
        else:
            d = num_list.index(_id)
            num1 = findStr(data,sub,d+1)
            num2 = findStr(data,sub,d+2)
            data2 = data[:num1] + data[num2:]
            f.seek(0)
            f.truncate()
            f.write(data2)
            print("information of id %s has been deleted" % _id)
            print("\033[31;1mmust quit the whole program next!!\033[0m")
def findStr(string, subStr, findCnt):
    listStr = string.split(subStr, findCnt)
    if len(listStr) <= findCnt:
        return -1
    return len(string) - len(listStr[-1]) - len(subStr)


with open("staff_table","r+") as f:
    while True:
        choice = input("inquire/create/delete/modify?>>")
        if choice == "q":
            break
        if choice == "inquire":
            inquire()
        if choice == "create":
            create()
        if choice == "delete":
            delete()
