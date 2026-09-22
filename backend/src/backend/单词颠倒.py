sentence = input("请输入一个字符串：")
sentence_finally = ""
for word in sentence.split():
    sentence_finally = word + " " + sentence_finally

print(sentence_finally)
