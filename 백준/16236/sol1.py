import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(s):

    visited = [[0] * N for _ in range(N)]
    Q = deque()
    Q.append(s)
    shark = 2
    eat = 0
    time = 0
    visited[s[0]][s[1]] = 1
    fish[s[0]][s[1]] = 0
    tmp = []

    # 상 좌 우 하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while Q:
        x, y = Q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < N and (fish[nx][ny] == shark or fish[nx][ny] == 0) and visited[nx][ny] == 0:
                Q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

            elif 0 <= nx < N and 0 <= ny < N and fish[nx][ny] < shark and visited[nx][ny] == 0:
                # Q.append([nx, ny])

                visited[nx][ny] = visited[x][y] + 1
                fish[nx][ny] = 0
                eat += 1
                time += visited[nx][ny] - 1

                if eat == shark:
                    shark += 1
                    eat = 0

                print([nx, ny], time, shark)
                visited = [[0] * N for _ in range(N)]
                Q = deque()
                Q.append([nx, ny])
                visited[nx][ny] = 1

                break

    return time


N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if fish[r][c] == 9:
            baby = [r, c]

print(bfs(baby))