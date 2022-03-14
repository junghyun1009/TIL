from collections import deque

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1

    return cnt

rlt = 0
tmp = []

for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and not visited[i][j]:
            rlt += 1
            tmp.append(bfs(i, j))

tmp = sorted(tmp)
print(rlt)
for i in tmp:
    print(i)
