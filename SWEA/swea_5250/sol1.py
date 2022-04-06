import sys

sys.stdin = open('input.txt')


def bfs(sr, sc, er, ec):

    Q = []
    Q.append([sr, sc])      # 큐에 시작점 넣어줌
    fuel[sr][sc] = H[sr][sc]        # 연료 시작점 초기화

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while Q:
        r, c = Q.pop(0)

        for dir in range(4):
            nr = r + dr[dir]
            nc = c + dc[dir]

            if 0 <= nr < N and 0 <= nc < N:     # 이동할 곳이 인덱스의 범위를 벗어나지 않는다면

                # 연료가 증가하고, 이동할 곳의 연료 소비량이 새로 계산한 연료 소비량보다 많다면 갱신
                if H[nr][nc] > H[r][c] and fuel[nr][nc] > fuel[r][c] + H[nr][nc] - H[r][c] + 1:
                    Q.append([nr, nc])
                    fuel[nr][nc] = fuel[r][c] + H[nr][nc] - H[r][c] + 1

                # 연료가 증가하지 않고, 이동할 곳의 연료 소비량이 새로 계산한 연료 소비량보다 많다면 갱신
                elif H[nr][nc] <= H[r][c] and fuel[nr][nc] > fuel[r][c] + 1:
                    Q.append([nr, nc])
                    fuel[nr][nc] = fuel[r][c] + 1

    return fuel[er][ec] - fuel[sr][sc]


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]

    fuel = [[10000] * N for _ in range(N)]
    
    print(f'#{tc} {bfs(0, 0, N-1, N-1)}')

