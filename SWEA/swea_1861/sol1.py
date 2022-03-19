import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(sx, sy):        # 각 방에서 상하좌우로 이동하면서 다음 방의 크기가 1 증가할 때 이동하며 갈 수 있는 방의 개수 탐색

    queue = deque()
    queue.append([sx, sy])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and room[nx][ny] == room[x][y] + 1:
                queue.append([nx, ny])
                cnt += 1
                break

    return cnt


T = int(input())

for tc in range(1, T + 1):

    n = int(input())        # n:방의 가로, 세로
    room = [list(map(int, input().split())) for _ in range(n)]      # 방 정보 저장
    visit = []      # 방문할 수 있는 방 개수를 저장할 리스트
    max_room = []       # 최대 방문 횟수를 만족하는 방을 저장할 리스트


    for i in range(n):
        for j in range(n):
            visit.append([bfs(i, j), room[i][j]])       # 각 방에 대해서 방문할 수 있는 방의 개수를 저장

    max_visit = max(visit)[0]       # 최대 방문 가능 횟수 저장

    for i in visit:
        if i[0] == max_visit:       # 최대 방문 가능 횟수를 만족하는 방의 번호 저장
            max_room.append(i[1])

    print(f'#{tc} {min(max_room)} {max_visit}')

