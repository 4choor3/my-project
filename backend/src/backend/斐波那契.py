f1 = f2 = 1
num = int(input("请输入一个正整数："))

if num == 1 or num == 2:
    fn = 1
else:
    while num > 2:
        fn = f1 + f2
        f1, f2 = f2, fn
        num -= 1

print(f"斐波那契数列的第{num}项是：{fn}")

