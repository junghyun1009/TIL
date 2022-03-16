import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

def bfs(start, end):
    queue = deque()
    queue.append(start)
    cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == 0:
                    queue.append([nx, ny])
                    maze[nx][ny] = maze[x][y] + 1


                elif maze[nx][ny] == 3 and (nx == end[0] and ny == end[1]):
                    return maze[x][y] - 2

    return 0

for tc in range(1, T + 1):

    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i, j]

            elif maze[i][j] == 3:
                end =[i, j]

    print(f'#{tc} {bfs(start, end)}')

