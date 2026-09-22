x = 1
for a in range(1, 101):
    x = 1
    for i in range(2, a):
        if a % i == 0:
            x = 0
    if x == 1:
        print(a)
