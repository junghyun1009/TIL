from pprint import pprint


def bfs(s, b):

    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        now = queue.pop(0)

        for i in range(1, n + 1):
            if graph[now][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[now] + 1

                if i == b:
                    return visited[i] - 1

    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())
family = [list(map(int, input().split())) for _ in range(m)]

graph = [[0] * (n + 1) for _ in range(n + 1)]

for f in family:
    graph[f[0]][f[1]] = 1
    graph[f[1]][f[0]] = 1

# pprint(graph)

visited = [0] * (n + 1)
print(bfs(a, b))