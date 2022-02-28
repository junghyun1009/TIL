a = [list(map(int, input().split())) for _ in range(4)]
b = [[0]*10 for _ in range(10)]

# for i in a:
#     for k in range(10 - i[3], 11 - i[1]):
#         for j in range(i[0], i[2]+1):
#             b[k][j] = 1

for i in a:
    for k in range(i[1], i[3]):
        for j in range(i[0], i[2]):
            b[k][j] = 1

cnt = 0
for i in b:
    for j in i:
        if j == 1:
            cnt += 1

print(cnt)