n = int(input())

a = []
for _ in range(n):
    a.append(list(map(int, input().split())))

a = sorted(a)
max_h = a[0][1]

for i in range(len(a)):
    if max_h <= a[i][1]:
        max_h = a[i][1]
        max_idx = i

area = max_h * (a[-1][0] - a[0][0] + 1)
width = 0

for i in range(max_idx):
    if a[i][1] < a[i+1][1]:
        width += a[i+1][0] - a[i][0]
        height = max_h - a[i][1]
        area -= width * height
        width = 0

    else:

        while a[i][1] >= a[i+1][1]:
            a[i+1][0] = a[i][0]
            a[i+1][1] = a[i][1]
            break


width = 0

for i in range(max_idx+1, len(a)-1):
    if a[i][1] > a[i+1][1]:
        width += a[i+1][0] - a[i][0]
        height = max_h - a[i][1]
        area -= width * height
        width = 0

    else:

        if a[i][1] <= a[i+1][1]:
            continue

print(area)