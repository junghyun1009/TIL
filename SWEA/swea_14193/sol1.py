import sys
from collections import deque
from pprint import pprint

sys.stdin = open('input.txt')


def bfs(sr, sc):

    # cnt = 0
    # visited = [[0] * X for _ in range(Y)]
    Q = deque()
    Q.append([sr, sc])
    visited[sr][sc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.popleft()

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == '_' and visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

            elif 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == 'A' and visited[nr][nc] == 0:
                Q.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                a = bfs(nr, nc)
                return visited[nr][nc] + a

                # cnt += visited[nr][nc] - 1
                # return ['A', visited[nr][nc] - 1]

            # elif 0 <= nr < Y and 0 <= nc < X and info[nr][nc] == 'S' and visited[nr][nc] == 0:
            #     Q.append([nr, nc])
            #     visited[nr][nc] = visited[r][c] + 1
            #     return ['S', visited[nr][nc] - 1]
    return 0


T = int(input())

for tc in range(1, T + 1):

    X, Y = map(int, input().split())
    info = [list(input()) for _ in range(Y)]
    visited = [[0] * X for _ in range(Y)]
    route = 0

    # for i in range(Y):
    #     for j in range(X):
    #         if info[i][j] == 'A' and visited[i][j] == 0:
    #             print(bfs(3, 1))
    print(bfs(3, 1))
    print(bfs(3, 1))

    # pprint(info)
    # print(bfs(3, 1))
    # pprint(visited)
    print(f'#{tc} {route}')

