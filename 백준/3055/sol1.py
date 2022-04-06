import sys

sys.stdin = open('input.txt')


def bfs(s):

    Q = []
    for i in s:
        Q.append(i)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.pop(0)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < R and 0 <= nc < C and


R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

water = []
for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':
            water.append([x, y])



print(water)

# print(forest)

