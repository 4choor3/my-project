num = int(input("请输入一个正整数："))

s = 0

for i in range(1, num + 1):
    s += i**2
print(s)
