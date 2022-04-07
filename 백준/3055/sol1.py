import sys

sys.stdin = open('input.txt')


def bfs(s):

    Q = []
    for i in s:
        Q.append(i)
        if i[2] == 2:
            visited[i[0]][i[1]] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c, n = Q.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            # 물이면
            if n == 1:
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == '.':
                    Q.append([nr, nc, 1])
                    forest[nr][nc] = '*'

                elif 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == 'S':
                    Q.append([nr, nc, 1])
                    forest[nr][nc] = '!'


            # 고슴도치면
            elif n == 2 and (forest[r][c] == 'S' or forest[r][c] == '!'):
                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == '.' and visited[nr][nc] == 0:
                    Q.append([nr, nc, 2])
                    forest[nr][nc] = 'S'
                    visited[nr][nc] = visited[r][c] + 1


                elif 0 <= nr < R and 0 <= nc < C and forest[nr][nc] == 'D':
                    return visited[r][c]

    return 'KAKTUS'


R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]

move = []

for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':
            move.append([x, y, 1])

for x in range(R):
    for y in range(C):
        if forest[x][y] == 'S':
            move.append([x, y, 2])

visited = [[0] * C for _ in range(R)]

# pprint(move)
print(bfs(move))
# pprint(visited)
# print(forest)

