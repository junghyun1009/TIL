num = [int(input()) for _ in range(10)]

remain = []
for i in num:
    remain.append(i % 42)

remain = set(remain)
print(len(remain))