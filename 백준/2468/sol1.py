import sys

sys.stdin = open('input.txt')


def bfs(x, y, h):
    queue = []
    queue.append([x, y])
    visited[x][y] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.pop(0)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and city[nr][nc] > h and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = 1

    return True


N = int(input())
city = [list(map(int, input.split())) for _ in range(N)]

rain = [0]

for i in range(N):
    for j in range(N):
        rain.append(city[i][j])

rain = list(set(rain))
# print(maxh)
# print(minh)
area = [0]

for i in rain:
    visited = [[0] * N for _ in range(N)]
    rlt = 0
    for j in range(N):
        for k in range(N):
            if city[j][k] > i and visited[j][k] == 0:
                if bfs(j, k ,i) == True:
                    rlt += 1
    area.append(rlt)
# print(area)
print(max(area))



