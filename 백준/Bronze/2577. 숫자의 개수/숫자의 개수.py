num = []
for _ in range(3):
    num.append(int(input()))

multiple = 1

for i in num:
    multiple *= i

multiple = str(multiple)

for j in range(10):
    print(multiple.count(str(j)))