def bfs(sr, sc):
    q = [[sr, sc]]
    visited[sr][sc] = 1

    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]

    while q:
        r, c = q.pop(0)
        for dir in range(8):
           nr = r + dr[dir]
           nc = c + dc[dir]

           if 0 <= nr < M and 0 <= nc < N and ground[nr][nc] == 1 and visited[nr][nc] == 0:
               q.append([nr, nc])
               visited[nr][nc] = 1

    return 1
    

M, N = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]
cnt = 0

for i in range(M):
    for j in range(N):
        if ground[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)