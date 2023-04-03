import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split(' '))
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
visited = [0] * (N+1)

def dfs(g, t):
    # visited[t] = 1
    for i in g[t]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(g, i)
    return

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        visited[i] = 1
        dfs(graph, i)
        cnt += 1

print(cnt)
