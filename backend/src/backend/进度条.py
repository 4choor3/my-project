import time

for num in range(0, 101, 10):
    bar = (
        "["
        + "#" * (int(num // 12.5))
        + " " * (8 - int(num // 12.5))
        + "]"
        + str(num)
        + "%"
    )
    print(bar, end="\r")
    time.sleep(0.5)
print("[########]100%")
