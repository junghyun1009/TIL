from collections import deque

def bfs(s):

    queue = deque()
    idx = []
    p = 0
    queue.append(s)
    idx.append(s)
    visited[s[0]][s[1]] = 1
    p += A[s[0]][s[1]]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                if L <= abs(A[nr][nc] - A[r][c]) <= R:
                    queue.append([nr, nc])
                    idx.append([nr, nc])
                    visited[nr][nc] = 1
                    p += A[nr][nc]

    move = p // len(idx)
    for i in idx:
        i.append(move)

    return idx


N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

while True:

    visited = [[0] * N for _ in range(N)]
    possible = []

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                a = bfs([i, j])
                if len(a) > 1:
                    possible.append(a)

    if len(possible) == 0:
        break

    # print(possible)
    for i in possible:
        for j in i:
            A[j[0]][j[1]] = j[2]

    cnt += 1

print(cnt)


