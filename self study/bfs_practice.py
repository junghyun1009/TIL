def bfs(s):

    Q = []
    Q.append(s)
    visited[s] = 1

    while Q:
        x = Q.pop(0)
        print(x, end=' ')
        for i in graph[x]:
            if visited[i] == 0:
                Q.append(i)
                visited[i] = 1


A = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

visited = [0] * 8
graph = [[] for _ in range(8)]

for i in range(0, len(A), 2):
    graph[A[i]].append(A[i+1])
    graph[A[i+1]].append(A[i])

bfs(1)