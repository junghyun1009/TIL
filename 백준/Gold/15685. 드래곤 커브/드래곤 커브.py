def dragon(a):

    stack = []
    tmp = []
    stack.append([a[0], a[1]])

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    stack.append([a[0] + dx[a[2]], a[1] + dy[a[2]]])
    tmp.append([a[0] + dx[a[2]], a[1] + dy[a[2]], a[2]])
    gen = 0

    while True:
        # print(gen, tmp)
        if gen == a[3]:
            return stack

        idx = len(tmp) - 1

        for i in range(len(tmp)):

            end = tmp[-1]
            end_d = tmp[idx][2]

            if 0 <= end_d <= 2:
                nd = end_d + 1
            else:
                nd = 0

            nx = end[0] + dx[nd]
            ny = end[1] + dy[nd]

            stack.append([nx, ny])
            tmp.append([nx, ny, nd])
            idx -= 1

        gen += 1


def square(a):

    cnt = 0
    x = a[0]
    y = a[1]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx <= 100 and 0 <= ny <= 100 and land[nx][ny] != 0:
            x = nx
            y = ny
            cnt += 1

        else:
            break

    if cnt == 4:
        return True
    else:
        return False


N = int(input())
curve = [list(map(int, input().split())) for _ in range(N)]
land = [[0] * 101 for _ in range(101)]
visited = [[0] * 101 for _ in range(101)]

# print(curve)
spot = []

for i in curve:
    dc = dragon(i)
    spot.extend(dc)
    for j in dc:
        land[j[0]][j[1]] = 1

rlt = 0
for i in spot:
    if visited[i[0]][i[1]] == 0 and square(i):
        # print(i)
        rlt += 1
        visited[i[0]][i[1]] = 1

print(rlt)