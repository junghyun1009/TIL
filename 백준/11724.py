import sys
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]

for i in a:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

cnt = 0
visited = [0] * (n + 1)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

for j in range(1, n+1):
    if visited[j] == 0:
        dfs(j)
        cnt += 1

print(cnt)
