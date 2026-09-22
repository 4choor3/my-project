list_test = [23, 5, 67, 67, 12, 89, 3, 89]
max_num = max(list_test)
count = list_test.count(max_num)
for _ in range(count):
    list_test.remove(max_num)
max_num2 = max(list_test)

print("第二大值为：", max_num2)
