import sys
from pprint import pprint

sys.stdin = open('input.txt')


def bfs(s):

    queue = []
    queue.append(s)
    cheese[s[0]][s[1]] = 2
    visited[s[0]][s[1]] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < R and 0 <= nc < C and cheese[nr][nc] != 1 and visited[nr][nc] == 0:
                queue.append([nr, nc])
                cheese[nr][nc] = 2
                visited[nr][nc] = 1


R, C = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(R)]
visited = [[0] * C for _ in range(R)]

# pprint(cheese)
bfs([0, 0])
# pprint(cheese)
cnt = 0

for r in range(R):
    for c in range(C):
        if cheese[r][c] == 1:
            cnt += 1

time = [cnt]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while cnt > 0:

    for r in range(R):
        for c in range(C):
            if cheese[r][c] == 2 and visited[r][c] == 1:
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]

                    if 0 <= nr < R and 0 <= nc < C and cheese[nr][nc] == 1:
                        cheese[nr][nc] = 2
                        visited[nr][nc] = 2
                        cnt -= 1
                        # bfs([nr, nc])

            # elif cheese[r][c] == 0:
            #     bfs([r, c])
    time.append(cnt)
    visited = [[0] * C for _ in range(R)]
    bfs([0, 0])

# pprint(cheese)
print(len(time)-1)
print(time[-2])
