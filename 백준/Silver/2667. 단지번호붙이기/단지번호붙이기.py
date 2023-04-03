from collections import deque
            
N = int(input())
home = [list(map(int, input())) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
blocks = []

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    cnt = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < N and home[nr][nc] == 1 and visited[nr][nc] == 0:
                q.append([nr, nc])
                visited[nr][nc] = 1
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if home[i][j] == 1 and visited[i][j] == 0:
            ans = bfs(i, j)
            blocks.append(ans)

blocks.sort()
print(len(blocks))
for k in blocks:
    print(k)