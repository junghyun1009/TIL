import sys

sys.stdin = open('input.txt')


def dfs(r, c, tmp, ssum):
    global msum

    if r == N:
        if ssum < msum:
            msum = ssum
        return msum

    if ssum > msum:
        return

    for i in range(0, N):
        if c not in tmp:
            tmp.append(c)
            dfs(r+1, i, tmp, ssum+num[r][c])
            tmp.pop()
    else:
        return


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    ssum = 0
    msum = 999999

    for i in range(N):
        tmp = []
        dfs(0, i, tmp, ssum)
    
    print(f'#{tc} {msum}')

