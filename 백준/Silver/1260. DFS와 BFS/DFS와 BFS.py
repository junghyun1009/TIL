from collections import deque

def dfs(g, s, v):
    print(s, end=' ')
    v[s] = 1
    for i in g[s]:
        if v[i] == 0:
            dfs(g, i, v)
    return

def bfs(g, s, v):
    q = deque()
    q.append(s)
    v[s] = 1
    while q:
        cur = q.popleft()
        print(cur, end=' ')
        for i in g[cur]:
            if v[i] == 0:
                q.append(i)
                v[i] = 1
    return

N, M, V = map(int, input().split(' '))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
visited = [0] * (N+1)
dfs(graph, V, visited)
print()
visited = [0] * (N+1)
bfs(graph, V, visited)

