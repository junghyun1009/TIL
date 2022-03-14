from collections import deque

m, n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(k)]
print(a)

graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for i in a:
    for j in range(i[0], i[2]):
        for k in range(i[1], i[3]):
            print(j, k)
            graph[j][k] = 1

print(graph)
