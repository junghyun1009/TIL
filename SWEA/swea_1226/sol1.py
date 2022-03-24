import sys

sys.stdin = open('input.txt')


def bfs(s, e):
    queue = []      # 경로를 기록할 큐
    queue.append(s)     # 출발점 추가
    visited[s[0]][s[1]] = 1     # 방문 표시

    dx = [-1, 1, 0, 0]      # 상, 하, 좌, 우 탐색
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)     # 큐의 첫번째 원소를 꺼내서 저장

        if x == e[0] and y == e[1]:     # 도착점에 도달했다면 1 반환
            return 1

        else:
            for dir in range(4):
                nx = x + dx[dir]
                ny = y + dy[dir]

                # 미로의 범위 안에 있고, 벽이 아니면서, 방문하지 않았다면
                if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1 and visited[nx][ny] == 0:
                    queue.append([nx, ny])      # 큐에 추가
                    visited[nx][ny] = 1     # 방문 표시

    return 0        # 더 이상 갈 길이 없다면 0 반환


for tc in range(1, 11):

    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:     # 출발 지점 찾기
                start = [i, j]
            elif maze[i][j] == 3:       # 도착 지점 찾기
                end = [i, j]
    
    print(f'#{tc} {bfs(start, end)}')

