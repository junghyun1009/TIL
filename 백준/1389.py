def bfs(s, g):

    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.pop(0)

        for i in range(N+1):
            if graph[x][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1
                if i == g:
                    return visited[i] - 1

    return 0


N, M = map(int, input().split())
rel = [list(map(int, input().split())) for _ in range(M)]

graph = [[0] * (N+1) for _ in range(N+1)]
for i in rel:
    graph[i[0]][i[1]] = 1
    graph[i[1]][i[0]] = 1

rlt = []

for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        visited = [0] * (N+1)
        tmp += bfs(i, j)
    rlt.append(tmp)

idx = []

for i in range(N):
    if rlt[i] == min(rlt):
        idx.append(i)

print(min(idx)+1)