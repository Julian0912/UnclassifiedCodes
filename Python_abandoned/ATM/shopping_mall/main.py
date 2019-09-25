# 未完成

balance = int(input("Your balance?--->"))
info = []
goods = [
    [1,"watch",30],
    [2,"lamp",20],
    [3,"PC",2000],
    [4,"textbooks",150],
    [5,"bluetooth",99],
    [6,"bag",29]
         ]
len2 = len(goods)
print("Available Goods Below!")
for i in goods:
    print(i)
print("-->Your balance is ",balance)
while True:
    _choice = int(input("Your choice is number(Input '0' to quit!):"))
    if _choice == 0:
        _len = len(info)
        if _len != 0:
            print("All goods below!")
            for a in info:
                print(a)
            print("-->Your balance is ",balance)
            print("Have a happy day!")
        else:
            print("-->Your balance is ", balance)
            print("Have a happy day!")
        break
    if _choice > len2 or _choice < 1:
        print("Please choose available goods!")
        continue
    choice = _choice - 1
    good = goods[choice]
    if good[2]>balance:
        print("Insufficient Balance!")
    else:
        balance = balance - good[2]
        info.append(good)
        print("You have bought the",good[1],"!")