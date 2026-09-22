line = int(input("请输入菱形的行数（奇数）："))


half = line // 2  # 中间行的索引，也是上半部分（含中间行）的行数 - 1

# 上半部分（包括中间行）
for i in range(half + 1):
    spaces = " " * (half - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# 下半部分（不包括中间行）
for i in range(half - 1, -1, -1):
    spaces = " " * (half - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
