num_1 = int(input("请输入一个数字："))
num_2 = int(input("请输入另一个数字："))
num_max = max(num_1, num_2)
num_list = []
for i in range(1, num_max + 1):
    if num_1 % i == 0 and num_2 % i == 0:
        num_list.append(i)

print(max(num_list))
