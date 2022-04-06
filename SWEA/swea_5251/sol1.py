import sys

sys.stdin = open("input.txt")


def dijkstra(s, V):
    visited = [0] * (V + 1)

    visited[s] = 1
    for i in range(V + 1):
        D[i] = adj[s][i]

    for _ in range(V):
        minV = INF
        w = 0

        for i in range(V + 1):
            if not visited[i] and minV > D[i]:
                w = i
                minV = D[i]

        visited[w] = 1
        for i in range(V + 1):
            if 0 < adj[w][i] < INF:
                D[i] = min(D[i], D[w] + adj[w][i])


T = int(input())

for tc in range(1, T + 1):

    INF = 999999999
    V, E = map(int, input().split())
    adj = [[INF] * (V + 1) for _ in range(V + 1)]

    for i in range(V + 1):
        adj[i][i] = 0

    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u][v] = w

    D = [0] * (V + 1)
    dijkstra(0, V)

    print(f'#{tc} {D[-1]}')