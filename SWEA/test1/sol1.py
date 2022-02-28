import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    max_rlt = 0

    for r in range(n):
        rlt = 0
        for c in range(r, r+k):
            if 0 <= c < n:
                rlt += a[r][c]
        if max_rlt < rlt:
            max_rlt = rlt

    print(f'#{tc} {max_rlt}')
