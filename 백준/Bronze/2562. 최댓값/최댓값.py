num = []
for _ in range(9):
    num.append(int(input()))

max_num = max(num)
max_idx = num.index(max_num) + 1

print(max_num)
print(max_idx)