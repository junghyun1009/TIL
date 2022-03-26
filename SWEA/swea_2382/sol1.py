import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(k)]

    # 일단 미생물 처음 위치 저장
    # 상, 하, 좌, 우에에 맞게 델타 설정
    # bfs (동시에 이동하니까)
    # 근데 얘는 영역 표시하면서 다니면 안될 것 같음
    # 테두리에 닿으면 절반으로 바꾸고 반대방향
    # 여러 군집이 합쳐졌을 때 방향 설정

    germs = [[[] for _ in range(n)] for _ in range(n)]
    # for i in range(n):
    #     for j in range(n):
    #         if i == 0 or i == n-1 or j == 0 or j == n-1:
    #             germs[i][j] = -1

    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    t = 0
    dir = []

    for i in a:
        germs[i[0]][i[1]] = i

    # while True:
    #     if t == m:
    #         break
    #
    #     for i in a:
    #         nx = i[0] + dx[i[3]]
    #         ny = i[1] + dy[i[3]]
    #
    #         if nx == 0 or nx == n-1 or ny == 0 or ny == n-1:
    #             germs[nx][ny] += germs[i[0]][i[1]] // 2
    #             germs[i[0]][i[1]] = 0
    #
    #             if i[3] == 1:
    #                 i[3] = 2
    #             elif i[3] == 2:
    #                 i[3] = 1
    #             elif i[3] == 3:
    #                 i[3] = 4
    #             else:
    #                 i[3] = 3
    #
    #         elif germs[nx][ny] == 0:
    #             germs[nx][ny] += germs[i[0]][i[1]]
    #             dir.append([germs[i[0]][i[1]], i[3]])
    #             germs[i[0]][i[1]] = 0
    #
    #         else:
    #
    #

    pprint(germs)

    print(f'#{tc} ')

