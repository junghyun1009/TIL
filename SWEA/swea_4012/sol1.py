import sys

sys.stdin = open('input.txt')


def dfs(s):

    if len(tmp) == num:
        copy = tmp[:]
        rlt.append(copy)
        return rlt

    for i in range(s, n):
        if i not in tmp:
            tmp.append(i)
            dfs(i+1)
            tmp.pop()


T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    food = [list(map(int, input().split())) for _ in range(n)]

    num = n / 2

    tmp = [0]
    rlt = []
    dfs(0)
    print(rlt)


    
    print(f'#{tc} ')

