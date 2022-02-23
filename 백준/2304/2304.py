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

height = a[0][1]
area = 0

for j in range(max_idx):
    width = 0

    if a[j][1] < a[j+1][1]:
        width += a[j+1][0] - a[j][0]
        area += height * width
        height = a[j+1][1]
        # print(j, area)

    elif a[j][1] >= a[j+1][1]:
        a[j+1][0] = a[j][0]
        a[j+1][1] = a[j][1]

print(area)

k = max_idx + 1
width = a[k][0] - a[max_idx][0]

while True:
    if k == len(a) - 1:
        break

    if a[k][1] <= a[k+1][1]:
        width += a[k+1][0] - a[k][0]
        height = a[k+1][1]
        k += 1

    else:
        width += a[k+1][0] - a[k][0]
        height = a[k][1]
        k += 1

    area += width * height


print(a)
print(max_h)
print(max_idx)
print(area)
