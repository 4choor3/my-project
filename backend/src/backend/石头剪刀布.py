import random

random.choice(["石头", "剪刀", "布"])
num_computer = num_user = 0

while num_computer < 3 and num_user < 3:
    user = input("请输入石头、剪刀、布：")
    computer = random.choice(["石头", "剪刀", "布"])
    print("电脑出的是：", computer)
    if user == computer:
        print("平局")
    elif (
        (user == "石头" and computer == "剪刀")
        or (user == "剪刀" and computer == "布")
        or (user == "布" and computer == "石头")
    ):
        print("用户获胜")
        num_user += 1
    else:
        print("电脑获胜")
        num_computer += 1

if num_computer == 3:
    print("电脑最终获胜")
elif num_user == 3:
    print("用户最终获胜")

# 石头剪刀布
