import sys

sys.stdin = open('input.txt')

def dfs(r, c):

    if r < 0 or r >= b or c < 0 or c >= a:
        print(stack)
        return

    for i in range(r, b):
        for j in range(c, a):
            if cheese[i][j] == 0 and [i, j] not in stack:
                stack.append([i, j])
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)



    
a, b = map(int, input().split())    # a:세로, b:가로
cheese = [list(map(int, input().split())) for _ in range(a)]
visited = [[0] * b for _ in range(a)]
stack = []

dfs(0, 0)


