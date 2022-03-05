import sys
sys.setrecursionlimit(10000)

def dfs_R(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    if a[r][c] == 'R' and v[r][c] == 0:
        v[r][c] = 1

        dfs_R(r-1, c)
        dfs_R(r+1, c)
        dfs_R(r, c-1)
        dfs_R(r, c+1)
        return True

    return False

def dfs_B(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    if a[r][c] == 'B' and v[r][c] == 0:
        v[r][c] = 1

        dfs_B(r-1, c)
        dfs_B(r+1, c)
        dfs_B(r, c-1)
        dfs_B(r, c+1)
        return True

    return False

def dfs_G(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    if a[r][c] == 'G' and v[r][c] == 0:
        v[r][c] = 1

        dfs_G(r-1, c)
        dfs_G(r+1, c)
        dfs_G(r, c-1)
        dfs_G(r, c+1)
        return True

    return False

def dfs_RG(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    if (a[r][c] == 'G' or a[r][c] == 'R') and v[r][c] == 0:
        v[r][c] = 1

        dfs_RG(r-1, c)
        dfs_RG(r+1, c)
        dfs_RG(r, c-1)
        dfs_RG(r, c+1)
        return True

    return False

n = int(input())
a = [list(input()) for _ in range(n)]
v = [[0] * n for _ in range(n)]

rlt_a = 0
rlt_b = 0

for i in range(n):
    for j in range(n):
        if dfs_R(i, j) == True:
            rlt_a += 1
        elif dfs_B(i, j) == True:
            rlt_a += 1
        elif dfs_G(i, j) == True:
            rlt_a += 1

v = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if dfs_RG(i, j) == True:
            rlt_b += 1
        elif dfs_B(i, j) == True:
            rlt_b += 1

print(rlt_a, end=' ')
print(rlt_b)