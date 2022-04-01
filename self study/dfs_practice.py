def dfs(s):

    visited[s] = 1
    print(s, end=' ')

    for i in graph[s]:
        if visited[i] == 0:
            dfs(i)


A = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

visited = [0] * 8
graph = [[] for _ in range(8)]

for i in range(0, len(A), 2):
    graph[A[i]].append(A[i+1])
    graph[A[i+1]].append(A[i])

stack =[]
dfs(1)