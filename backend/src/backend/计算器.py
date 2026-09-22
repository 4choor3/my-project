while True:
    num_1 = int(input("请输入第一个整数："))
    symbol = input("请输入运算符：")
    num_2 = int(input("请输入第二个整数："))
    if symbol not in ["+", "-", "*", "/"]:
        print("输入的运算符不合法，请重新输入！")
        symbol = input("请输入运算符：")
    if symbol == "/" and num_2 == 0:
        print("除数不能为零，请重新输入！")
        num_2 = int(input("请输入第二个整数："))
    if num_1 == "q" or symbol == "q" or num_2 == "q":
        break

    print("计算结果为：", eval(str(num_1) + symbol + str(num_2)))
    
