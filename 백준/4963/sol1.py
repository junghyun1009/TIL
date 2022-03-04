import sys

sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if a[x][y] == 1:
        a[x][y] = 0

        dfs(x-1, y-1)
        dfs(x-1, y)
        dfs(x-1, y+1)
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        return True
    return False


while True:

    w, h = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    if w == 0 and h == 0:
        break
    

    rlt = 0
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                rlt += 1

    print(rlt)


