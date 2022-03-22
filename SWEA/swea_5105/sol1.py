import sys

sys.stdin = open('input.txt')


def bfs(start, end):        # 미로 길 탐색을 위한 bfs 함수
    queue = []      # 큐 생성
    queue.append(start)     # 시작점을 큐에 넣어준다

    dx = [-1, 1, 0, 0]      # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    while queue:        # 큐에 원소가 없을 때까지
        x, y = queue.pop(0)      # 큐의 가장 첫 원소 빼서 각각 저장

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:     # 이동할 인덱스가 미로 안의 범위라면
                if maze[nx][ny] == 0:       # 길이라면
                    queue.append([nx, ny])      # 큐에 넣어준다
                    maze[nx][ny] = maze[x][y] + 1       # 경로의 길이를 나타내기 위해 1씩 더해가며 이동한다


                elif maze[nx][ny] == 3 and (nx == end[0] and ny == end[1]):     # 도착지와 일치한다면
                    return maze[x][y] - 2       # 더해가며 이동하던 숫자에서 2 빼서 반환(출발을 2부터 했으므로)

    return 0        # 정상적으로 함수가 종료되지 않았다면 길 탐색에 실패한 것이므로 0 반환


T = int(input())

for tc in range(1, T + 1):

    n = int(input())        # n : 미로의 가로, 세로 길이
    maze = [list(map(int, input())) for _ in range(n)]      # 미로 받아오기

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:     # 출발지점 인덱스 찾아 저장
                start = [i, j]

            elif maze[i][j] == 3:       # 도착지점 인덱스 찾아 저장
                end = [i, j]

    print(f'#{tc} {bfs(start, end)}')

