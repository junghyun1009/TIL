from collections import deque

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
    mroute = 99999

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
                # tmp.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                if mroute >= visited[nx][ny]:
                    mroute = visited[nx][ny]
                    tmp.append([nx, ny])

        if len(Q) == 0:
            # print(tmp)
            if len(tmp) == 1:
                ax = tmp[0][0]
                ay = tmp[0][1]
                fish[ax][ay] = 0
                eat += 1
                time += visited[ax][ay] - 1
                if eat == shark:
                    shark += 1
                    eat = 0

                # print([ax, ay], time, shark)
                visited = [[0] * N for _ in range(N)]
                Q = deque()
                Q.append([ax, ay])
                visited[ax][ay] = 1
                tmp = []
                mroute = 99999

            elif len(tmp) > 1:
                tmp = sorted(tmp)
                ax = tmp[0][0]
                ay = tmp[0][1]
                fish[ax][ay] = 0
                eat += 1
                time += visited[ax][ay] - 1
                if eat == shark:
                    shark += 1
                    eat = 0

                # print([ax, ay], time, shark)
                visited = [[0] * N for _ in range(N)]
                Q = deque()
                Q.append([ax, ay])
                visited[ax][ay] = 1
                tmp = []
                mroute = 99999

    return time


N = int(input())
fish = [list(map(int, input().split())) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if fish[r][c] == 9:
            baby = [r, c]

print(bfs(baby))