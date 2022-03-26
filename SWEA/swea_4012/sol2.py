import sys

sys.stdin = open('input.txt')


def dfs(n, lst):

    if len(lst) == N/2:
        rlt.append(lst)
        return rlt

    elif n == N:
        return

    dfs(n+1, lst+[n])
    dfs(n+1, lst)


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    lst = [0]
    rlt = []
    dfs(1, lst)

    print(f'#{tc} {rlt}')

