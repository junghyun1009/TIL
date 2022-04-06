import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs():
    global cnt

    Q = deque()
    for t in tree:
        Q.append(t)

    a, b, c = Q.popleft()
    check[a][b] = 1
    check[b][a] = 1
    cnt += c

    while Q:
        r, c, w = Q.popleft()
        visited = [[0] * (V + 1) for _ in range(V + 1)]

        def cycle(x, y):

            if check[x][y] != 0:
                return True

            else:
                for i in range(V + 1):

                    if check[x][i] == 1 and visited[x][i] == 0:
                        visited[x][i] = 1
                        visited[i][x] = 1

                        if cycle(i, y):
                            if check[i][y] == 0:
                                check[i][y] = 1
                                check[y][i] = 1
                            return True

                return False

        if not cycle(r, c):
            check[r][c] = 1
            check[c][r] = 1
            cnt += w

        else:   # 싸이클 구조의 경우
            check[r][c] = 2
            check[c][r] = 2


T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    tree = [list(map(int, input().split())) for _ in range(E)]

    tree.sort(key=lambda x: x[2])

    check = [[0] * (V + 1) for _ in range(V + 1)]

    cnt = 0
    bfs()

    print(f'#{tc} {cnt}')

