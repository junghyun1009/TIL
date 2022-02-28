import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    max_rlt = 0

    for r in range(n):
        for c in range(n):
            rlt = a[r][c]
            for d in range(4):
                for p in range(1, m):
                    nr = r + dr[d] * p
                    nc = c + dc[d] * p
                    if 0 <= nr < n and 0 <= nc < n:
                        rlt += a[nr][nc]
                    else:
                        break
                if not(0 <= nr < n and 0 <= nc < n):
                    break
            if max_rlt < rlt:
                max_rlt = rlt

    # 왼위, 오위, 오아, 왼아
    dr = [-1, -1, 1, 1]
    dc = [-1, 1, 1, -1]
    max_rlt2= 0

    for r in range(n):
        for c in range(n):
            rlt = a[r][c]
            for d in range(4):
                for p in range(1, m):
                    nr = r + dr[d] * p
                    nc = c + dc[d] * p
                    if 0 <= nr < n and 0 <= nc < n:
                        rlt += a[nr][nc]
                    else:
                        break
                if not(0 <= nr < n and 0 <= nc < n):
                    break
            if max_rlt2 < rlt:
                max_rlt2 = rlt

    print(f'#{tc} {max_rlt} {max_rlt2}')

