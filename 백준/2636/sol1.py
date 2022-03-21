import sys
from pprint import pprint

sys.stdin = open('input.txt')

# 치즈 속 구멍 2로 바꿔주기
def dfs(i, j):
    stack = []
    hole = []
    if visited[i][j] == 0:
        stack.append([i, j])
        hole.append([i, j])
        visited[i][j] = 1

    while stack:
        i, j = stack.pop()
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]
            if 0 <= ni < r and 0 <= nj < c and cheese[ni][nj] == 0 and visited[ni][nj] == 0:
                stack.append([ni, nj])
                hole.append([ni, nj])
                visited[i][j] = 1

    for k in hole:
        if k[0] == 0 or k[0] == r-1 or k[1] == 0 or k[1] == c-1:
            break
    else:
        for h in hole:
            cheese[h[0]][h[1]] = 2


r, c = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(r)]
visited = [[0] * c for _ in range(r)]

for i in range(r):
    for j in range(c):
        if cheese[i][j] == 0:
            dfs(i, j)

pprint(cheese)