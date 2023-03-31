def bfs(s, e):

    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.pop(0)
        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == 1 and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1
                if [nr, nc] == e:
                    return visited[nr][nc]


N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

start = [0, 0]
end = [N-1, M-1]
visited = [[0] * M for _ in range(N)]
# print(maze)
print(bfs(start, end))