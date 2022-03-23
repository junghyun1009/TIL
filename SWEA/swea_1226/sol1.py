import sys

sys.stdin = open('input.txt')


def bfs(s, e):
    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)

        if x == e[0] and y == e[1]:
            return 1

        else:
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1

    return 0


for tc in range(1, 11):

    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                end = [i, j]
    
    print(f'#{tc} {bfs(start, end)}')

