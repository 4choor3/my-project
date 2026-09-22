gra=[85, 92, 78, 60, 95, 88]
avg=sum(gra) / len(gra)
max_=max(gra)
num =0
for grade in gra:
    if grade >= 60:
        num += 1
print("平均分：", avg)
print("最高分：", max_)
print("及格人数：", num)

