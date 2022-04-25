import sys
from pprint import pprint

sys.stdin = open('input.txt')

N, M = map(int, input().split())    # 세로, 가로
r, c, d = map(int, input().split())     # 현재 위치, 방향(북-동-남-서)
room = [list(map(int, input().split())) for _ in range(N)]
turn = 0

while True:
    if turn == 4:
        if d == 0:
            if room[r+1][c] == 1:
                break
            else:
                r = r + 1
                c = c
                turn = 0

        elif d == 1:
            if room[r][c-1] == 1:
                break
            else:
                r = r
                c = c - 1
                turn = 0

        elif d == 2:
            if room[r-1][c] == 1:
                break
            else:
                r = r - 1
                c = c
                turn = 0

        else:
            if room[r][c+1] == 1:
                break
            else:
                r = r
                c = c + 1
                turn = 0

    room[r][c] = 2
    # print([r, c], d)
    # 북쪽을 바라보고 있을 때
    if d == 0:
        # 바로 왼쪽에 빈 공간이 존재하면
        if room[r][c-1] == 0:
            r = r
            c = c - 1
            d = 3
            turn = 0
        else:
            d = 3
            turn += 1

    # 동쪽을 바라보고 있을 때
    elif d == 1:
        # 바로 왼쪽에 빈 공간이 존재하면
        if room[r-1][c] == 0:
            r = r - 1
            c = c
            d = 0
            turn = 0
        else:
            d = 0
            turn += 1

    # 남쪽을 바라보고 있을 때
    elif d == 2:
        # 바로 왼쪽에 빈 공간이 존재하면
        if room[r][c+1] == 0:
            r = r
            c = c + 1
            d = 1
            turn = 0
        else:
            d = 1
            turn += 1

    # 서쪽을 바라보고 있을 때
    else:
        # 바로 왼쪽에 빈 공간이 존재하면
        if room[r+1][c] == 0:
            r = r + 1
            c = c
            d = 2
            turn = 0
        else:
            d = 2
            turn += 1

pprint(room)
cnt = 0
for i in room:
    for j in i:
        if j == 2:
            cnt += 1

print(cnt)

