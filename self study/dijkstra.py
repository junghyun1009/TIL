import sys

sys.stdin = open("input.txt")


def dijkstra(s, V):
    visited = [0] * (V + 1)

    visited[s] = 1
    for i in range(V + 1):
        D[i] = adj[s][i]  # 초기 D 리스트 만들기

    for _ in range(V):
        minV = INF  # 선택된 목적지까지 가는 가중치
        w = 0  # 이번에 선택된 목적지

        # 방문하지 않은 노드 중에서, 가장 비용이 적은 노드 선택
        for i in range(V + 1):
            if not visited[i] and minV > D[i]:
                w = i
                minV = D[i]

        visited[w] = 1  # 방문 표시
        for i in range(V + 1):
            if 0 < adj[w][i] < INF:  # 연결되어있으면
                D[i] = min(D[i], D[w] + adj[w][i])


INF = 987654321
V, E = map(int, input().split())
adj = [[INF] * (V + 1) for _ in range(V + 1)]

for i in range(V + 1):
    adj[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u][v] = w

D = [0] * (V + 1)
dijkstra(0, V)

print(D)