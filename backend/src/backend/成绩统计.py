list_score = [85, 92, 78, 60, 95, 45, 88, 72, 59, 91]
num_up = 0
num_medium = 0
num_low = 0
num_down = 0

for score in list_score:
    if score >= 90:
        num_up += 1
    elif score >= 80:
        num_medium += 1
    elif score >= 60:
        num_low += 1
    else:
        num_down += 1
print(f"90+:{num_up}人")
print(f"80-89:{num_medium}人")
print(f"60-79:{num_low}人")
print(f"60一下:{num_down}人")
