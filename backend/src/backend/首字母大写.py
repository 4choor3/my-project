sentence = input("请输入一个字符串：")
# 字符串转换

# 神奇方法
sentence_finally = ""

for word in sentence.split():
    sentence_finally += word[0].upper() + word[1:] + " "
print(sentence_finally)

# 正常方法
print(sentence.title())
