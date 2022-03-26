import sys

sys.stdin = open('input.txt')


def dfs(n, ssum):
    global ans

    if ssum >= B:
        if ans > ssum - B:
            ans = ssum - B
            return ans

    if n == N:
        return

    dfs(n+1, ssum + S[n])
    dfs(n+1, ssum)


T = int(input())

for tc in range(1, T + 1):

    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    ans = 9999999999

    dfs(0, 0)
    
    print(f'#{tc} {ans}')

