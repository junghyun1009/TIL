import sys

sys.stdin = open('input.txt')


def dfs(a):
    if len(a) == 2:
        rlt.append(a)
        return

    for i in range(1, N-1):
        dfs(a + [i])


def bfs(sr, sc):
    global maxcnt

    # Q = []
    # Q.append([sr, sc])
    dessert[cafe[sr][sc]] = 1

    # 오아 왼아 왼위 오위
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    # while Q:
    #     r, c = Q.pop(0)

    for each in rlt:
        w = each[0]
        h = each[1]
        flag = 1

        if sr + w + h < N and sc + w < N:
            for dir in range(4):
                if flag == 0:
                    break

                if dir % 2 == 0:
                    for _ in range(w):
                        nr = sr + dr[dir]
                        nc = sc + dc[dir]

                        if dessert[cafe[nr][nc]] == 0:
                            dessert[cafe[nr][nc]] = 1
                            sr = nr
                            sc = nr

                        else:
                            flag = 0
                            break

                else:
                    for _ in range(h):
                        nr = sr + dr[dir]
                        nc = sc + dc[dir]

                        if dessert[cafe[nr][nc]] == 0:
                            dessert[cafe[nr][nc]] = 1
                            sr = nr
                            sc = nr

                        else:
                            flag = 0
                            break

        rlt = 2 * (w + h)
        if maxcnt < rlt:
            maxcnt = rlt



T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    dessert = [0] * 101
    maxcnt = 0

    rlt = []
    visited = [0] * (N - 1)
    dfs([])
    print(rlt)

    print(f'#{tc} ')

