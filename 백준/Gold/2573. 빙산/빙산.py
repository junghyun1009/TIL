import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split(' '))
ice = [list(map(int, input().split(' '))) for _ in range(N)]

ans = 0
Y = 0

while True:
    ice_copy = [arr[:] for arr in ice]
    # 1년 지난 후 빙하
    Y += 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for r in range(N):
        for c in range(M):
            ocean = 0
            if ice_copy[r][c] != 0:
                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]

                    if 0 <= nr < N and 0 <= nc < M and ice_copy[nr][nc] == 0:
                        ocean += 1

                        if ice_copy[r][c] - ocean >= 0:
                            ice[r][c] = ice_copy[r][c] - ocean
                        else:
                            ice[r][c] = 0

    # print(ice)
    # 몇 덩어리인지 계산
    visited = [[0] * M for _ in range(N)]
    q = deque()
    cnt = 0
    icesum = 0
    for r in range(N):
        for c in range(M):
            icesum += ice[r][c]
            if ice[r][c] != 0 and visited[r][c] == 0:
                q.append([r, c])
                visited[r][c] = 1
                while q:
                    cr, cc = q.popleft()
                    for dir in range(4):
                        nr = cr + dr[dir]
                        nc = cc + dc[dir]

                        if 0 <= nr < N and 0 <= nc < M and ice[nr][nc] != 0 and visited[nr][nc] == 0:
                            q.append([nr, nc])
                            visited[nr][nc] = 1
                cnt += 1

    if cnt >= 2:
        ans = Y
        break

    if icesum == 0:
        break

print(ans)
