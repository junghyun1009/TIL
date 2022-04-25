import sys

sys.stdin = open('input.txt')


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

route_list = []
for i in chicken:
    route = 0
    for j in house:
        route += abs(i[0]-j[0]) + abs(i[1]-j[1])
    route_list.append([route, i])
route_list.sort()
print(route_list)

rlt_list = route_list[0 : M]
print(rlt_list)

rlt = 0
for i in house:
    min_route = 999999
    for j in rlt_list:
        tmp = abs(i[0]-j[1][0]) + abs(i[1]-j[1][1])
        if min_route > tmp:
            min_route = tmp
    rlt += min_route

print(rlt)
