sentence= input("请输入一个字符串："  )

ae = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
num = 0
for word in sentence:
    if word in ae:
        num+= 1

print(num)
