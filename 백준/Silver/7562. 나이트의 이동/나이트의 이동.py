def bfs(s, e):

    queue = []
    queue.append(s)
    visited[s[0]][s[1]] = 1

    dr = [-2, -1, 1, 2, 2, 1, -1, -2]
    dc = [1, 2, 2, 1, -1, -2, -2, -1]

    while queue:
        r, c = queue.pop(0)

        for dir in range(8):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < I and 0 <= nc < I and visited[nr][nc] == 0:
                queue.append([nr, nc])
                visited[nr][nc] = visited[r][c] + 1

                if [nr, nc] == e:
                    return visited[nr][nc] - 1

    return 0

T = int(input())

for tc in range(1, T+1):

    I = int(input())
    S = list(map(int, input().split()))
    E = list(map(int, input().split()))

    visited = [[0] * I for _ in range(I)]
    print(bfs(S, E))

