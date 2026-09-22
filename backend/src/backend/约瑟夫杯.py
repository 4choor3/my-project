n = int(input("人数："))
people = list(range(1, n + 1))
result = []
index = 0

while people:
    index = (index + 2) % len(people)
    result.append(people.pop(index))

print("出列顺序：", " ".join(map(str, result)))
