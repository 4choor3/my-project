num = input("请输入一个正整数：")
total = num

while len(num) > 1:
    total = 0
    for ch in range(len(num)):
        num_single = int(num[ch])
        total += num_single
    num = str(total)


print("该数的各位数字之和是：", total)
