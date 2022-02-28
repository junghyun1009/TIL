import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    rlt_a = []

    for r in range(n):
        for c in range(n):
            rlt = 0
            for d in range(9):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < n and 0 <= nc < n:
                   rlt += a[nr][nc]
                else:
                    rlt = 0
                    break
            rlt_a.append(rlt)

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for r in range(n):
        for c in range(n):
            rlt = a[r][c]
            for d in range(4):
                for p in range(1, a[r][c]):
                    nr = r + dr[d] * p
                    nc = c + dc[d] * p
                    if 0 <= nr < n and 0 <= nc < n:
                        rlt += a[nr][nc]
            rlt_a.append(rlt)

    print(f'#{tc} {max(rlt_a)}')