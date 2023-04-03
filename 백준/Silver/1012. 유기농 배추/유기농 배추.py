from collections import deque

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split(' '))
    cab = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split(' '))
        cab[Y][X] = 1
    # print(cab)

    cnt = 0
    visited = [[0] * M for _ in range(N)]

    def bfs(r, c):
        global cnt
        q = deque()
        q.append([r, c])
        visited[r][c] = 1

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while q:
            cr, cc = q.popleft()
            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]

                if 0 <= nr < N and 0 <= nc < M and cab[nr][nc] == 1 and visited[nr][nc] == 0:
                    q.append([nr, nc])
                    visited[nr][nc] = 1

        cnt += 1
        return cnt

    for i in range(N):
        for j in range(M):
            if cab[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)

    print(cnt)