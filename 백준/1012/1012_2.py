import sys

sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)

# 큰 덩어리의 갯수만 알 수 있음
def dfs(r, c, v):

    if r < 0 or r >= N or c < 0 or c >= M:
        return False

    elif v[r][c] == 1 or graph[r][c] == 0:
        return False

    if graph[r][c] == 1:
        v[r][c] = 1

        dfs(r-1, c, v)
        dfs(r+1, c, v)
        dfs(r, c-1, v)
        dfs(r, c+1, v)

        return True

    # return False


T = int(input())

for tc in range(1, T+1):

    M, N, K = map(int, input().split())
    cab = [list(map(int, input().split())) for _ in range(K)]

    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for i in cab:
        graph[i[1]][i[0]] = 1

    rlt = 0

    for i in range(N):
        for j in range(M):
            if dfs(i, j, visited) == True:
                rlt += 1

    print(rlt)