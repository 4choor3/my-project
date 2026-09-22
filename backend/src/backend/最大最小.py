list = [23, 5, 67, 12, 89, 3]
max_ = list[0]
for i in list:
    max_ = max(max_, i)
print(max_)

min_ = list[0]
for i in list:
    min_ = min(min_, i)
print(min_)
