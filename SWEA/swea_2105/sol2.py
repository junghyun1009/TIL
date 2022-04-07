import sys

sys.stdin = open('input.txt')


def bfs(sr, sc):
    global cnt

    Q = []
    Q.append([sr, sc])
    dessert[cafe[sr][sc]] = 1

    # 오아 왼아 왼위 오위
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    while Q:
        r, c = Q.pop(0)

        for a in range(1, N - 1):
            for b in range(1, N - 1):
                for dir in range(4):
                    if dir % 2 == 0:
                        for i in range(1, a+1):
                            nr = r + dr[dir] * a
                            nc = c + dc[dir] * a

                            if 0 <= nr < N and 0 <= nc < N and dessert[cafe[nr][nc]] == 0:
                                cnt += 1
                            else:
                                break


                    else:
                        nr = r + dr[dir] * b
                        nc = c + dc[dir] * b




T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    dessert = [0] * 101
    cnt = 0
    print(f'#{tc} ')

