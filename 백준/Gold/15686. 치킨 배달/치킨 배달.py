from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

chicken = []
house = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 1:
            house.append([r, c])
        elif city[r][c] == 2:
            chicken.append([r, c])

pick = list(combinations(chicken, M))
# print(pick)

min_rlt = 999999
for i in pick:
    rlt = 0
    for j in house:
        min_route = 999999
        for k in i:
            tmp = abs(k[0] - j[0]) + abs(k[1] - j[1])
            if min_route > tmp:
                min_route = tmp
        rlt += min_route
    if min_rlt > rlt:
        min_rlt = rlt
print(min_rlt)