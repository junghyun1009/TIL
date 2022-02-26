import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    num = []

    for r in range(n):
        cnt = 0
        check = 0
        for c in range(n):
            if a[r][c] == 1:
                cnt += 1
                check = 1
                if c == n - 1:
                    num.append(cnt)
            else:
                if check == 1:
                    num.append(cnt)
                    cnt = 0
                    check = 0


    for c in range(n):
        cnt = 0
        check = 0
        for r in range(n):
            if a[r][c] == 1:
                cnt += 1
                check = 1
                if r == n - 1:
                    num.append(cnt)
            else:
                if check == 1:
                    num.append(cnt)
                    cnt = 0
                    check = 0

    rlt = num.count(k)

    print(f'#{tc} {rlt}')

