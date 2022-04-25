import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(s):
    Q = deque()
    # num = s[2]
    for i in s:
        Q.append(i)
        visited[i[0]][i[1]] = i[2]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    time = 0

    while Q:

        if time == S:
            return visited[X-1][Y-1]
        # print(Q)
        # print(time)
        r, c, num = Q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                Q.append([nr, nc, num])
                visited[nr][nc] = num

        if num == K and Q[0][2] != K:
            time += 1
            # print(num, time)
            if time == S:
                return visited[X-1][Y-1]

    return visited[X-1][Y-1]


N, K = map(int, input().split())    # N:행 수, K:바이러스 번호
virus = [list(map(int, input().split())) for _ in range(N)]     # 바이러스 지도
S, X, Y = map(int, input().split())     # 시간, 도착 X, 도착 Y

visited = [[0] * N for _ in range(N)]
place = []

for r in range(N):
    for c in range(N):
        if virus[r][c] != 0:
            place.append([r, c, virus[r][c]])

place.sort(key=lambda x: x[2])
# print(place)
rlt = bfs(place)
print(rlt)

