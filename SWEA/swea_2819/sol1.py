import sys

sys.stdin = open('input.txt')


def dfs(x, y):
    if len(tmp) == 7:
        if tmp not in rlt:
            rlt.append(tmp)
            print(tmp)
            tmp.pop()
            return

        else:
            tmp.pop()
            return

    if x < 0 or x >= 4 or y < 0 or y >= 4:
        return

    tmp.append(num[x][y])
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    tmp.pop()
    return


T = int(input())

for tc in range(1, T + 1):

    num = [list(map(int, input().split())) for _ in range(4)]
    tmp = []
    rlt = []

    dfs(0, 0)
    
    print(f'#{tc} ')

