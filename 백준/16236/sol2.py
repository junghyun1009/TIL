# 성공!
import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(s):
    visited = [[0] * N for _ in range(N)]       # 상어 방문 표시
    Q = deque()
    Q.append(s)
    shark = 2       # 상어 크기
    eat = 0     # 상어가 먹은 물고기
    time = 0        # 상어가 먹은 시간
    visited[s[0]][s[1]] = 1     # 출발 지점 방문 표시
    fish[s[0]][s[1]] = 0        # 출발 지점 초기화
    tmp = []        # 먹을 수 있는 물고기 담을 리스트
    mroute = 99999      # 최단 거리 측정하기 위한 변수

    # 상 좌 우 하
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    while Q:
        x, y = Q.popleft()

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            # 이동만 할 수 있는 경우(물고기가 없거나 상어 크기와 같은 물고기가 있거나)
            if 0 <= nx < N and 0 <= ny < N and (fish[nx][ny] == shark or fish[nx][ny] == 0) and visited[nx][ny] == 0:
                Q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

            # 물고기를 먹을 수 있는 경우(상어 크기보다 작은 물고기가 있는 경우)
            elif 0 <= nx < N and 0 <= ny < N and fish[nx][ny] < shark and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                # 최단 경로 갱신 / 최단 경로인 경우에만 먹을 수 있는 물고기 리스트에 추가
                if mroute >= visited[nx][ny]:
                    mroute = visited[nx][ny]
                    tmp.append([nx, ny])

        if len(Q) == 0:     # 큐에 있는 모든 원소를 확인했다면
            # print(tmp)
            if len(tmp) == 1:       # 먹을 수 있는 물고기가 한 마리라면
                ax = tmp[0][0]      # 물고기 위치 저장
                ay = tmp[0][1]
                fish[ax][ay] = 0        # 물고기 먹기
                eat += 1        # 먹은 물고기 한 마리 추가
                time += visited[ax][ay] - 1     # 이동한 시간 저장
                if eat == shark:        # 상어의 크기만큼 먹었다면
                    shark += 1      # 상어의 크기 1 증가
                    eat = 0     # 먹은 물고기 수 초기화

                # print([ax, ay], time, shark)
                visited = [[0] * N for _ in range(N)]       # 초기화
                Q = deque()
                Q.append([ax, ay])
                visited[ax][ay] = 1
                tmp = []
                mroute = 99999

            elif len(tmp) > 1:      # 먹을 수 있는 물고기가 여러 마리라면
                tmp = sorted(tmp)       # 위-왼쪽 물고기가 가장 우선순위
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