import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

# 각 덩어리의 갯수도 알 수 있음
def dfs(r, c, v):
    global cnt

    if r < 0 or r >= N or c < 0 or c >= M:
        return

    elif v[r][c] == 1 or graph[r][c] == 0:
        return

    v[r][c] = 1
    cnt += 1

    dfs(r-1, c, v)
    dfs(r+1, c, v)
    dfs(r, c-1, v)
    dfs(r, c+1, v)
    return cnt


T = int(input())

for tc in range(1, T+1):

    M, N, K = map(int, input().split())
    cab = [list(map(int, input().split())) for _ in range(K)]

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in cab:
        graph[i[1]][i[0]] = 1

    rlt = []

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                cnt = 0
                dfs(i, j, visited)
                if cnt != 0:
                    rlt.append(cnt)

    print(len(rlt))