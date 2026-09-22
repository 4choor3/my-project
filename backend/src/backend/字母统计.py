sentence = input("请输入一个字符串："  )
sum_words = {}

for word in sentence:
    sum_words[word] = sum_words.get(word, 0) + 1

print(sum_words)
