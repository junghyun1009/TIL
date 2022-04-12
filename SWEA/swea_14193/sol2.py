import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt')


def bfs(sr, sc):

    Q = []
    A = []
    Q.append([sr, sc])
    A.append([sr, sc])
    visited = [[0] * X for _ in range(Y)]
    visited[sr][sc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.pop(0)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == '_' and visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

            elif 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == 'A' and visited[nr][nc] == 0:
                Q.append([nr, nc])
                A.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

            elif 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == 'S' and visited[nr][nc] == 0:
                ans = visited[r][c] + 1
                return [ans - 1, A]

    return [0, A]


T = int(input())

for tc in range(1, T + 1):

    X, Y = map(int, input().split())
    info = [list(input()) for _ in range(Y)]
    visited = [[0] * X for _ in range(Y)]
    rlt = 0

    for i in range(Y):
        for j in range(X):
            # visited = [[0] * X for _ in range(Y)]
            if info[i][j] == 'A' and visited[i][j] == 0:
                tmp = bfs(i, j)
                print(tmp)

    print(f'#{tc} ')

