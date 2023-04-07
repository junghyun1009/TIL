import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split(' '))
room = [list(map(int, input().split(' '))) for _ in range(N)]

cctv_a = [['n'], ['e'], ['s'], ['w']]
cctv_b = [['n', 's'], ['e', 'w']]
cctv_c = [['n', 'e'], ['e', 's'], ['s', 'w'], ['w', 'n']]
cctv_d = [['w', 'n', 'e'], ['n', 'e', 's'], ['e', 's', 'w'], ['s', 'w', 'n']]
cctv_e = [['n', 'e', 's', 'w']]
num = [0, 4, 2, 4, 4, 1]

# cctv 파악
cctv = []
place= []
for r in range(N):
    for c in range(M):
        if (room[r][c] != 0) and (room[r][c] != 6):
            cctv.append(room[r][c])
            place.append([r, c])

# 감시 경로 수열
def route(arr, rlt):
    if len(arr) == len(cctv):
        rlt.append(arr)
        return
    cur = len(arr)
    for i in range(num[cctv[cur]]):
        route(arr+[i], rlt)

rlt = []
route([], rlt)
# print(rlt)

# 각 경우 파악하면서 최소 사각지대 찾기
minimum = 999999

for each in rlt:
    room_copy = [arr[:] for arr in room]
    for i in range(len(each)):
        # 감시 방향 확정
        if cctv[i] == 1:
            direction = cctv_a[each[i]]
        elif cctv[i] == 2:
            direction = cctv_b[each[i]]
        elif cctv[i] == 3:
            direction = cctv_c[each[i]]
        elif cctv[i] == 4:
            direction = cctv_d[each[i]]
        else:
            direction = cctv_e[each[i]]

        for d in direction:
            if d == 'n':
                dir = 0
            elif d == 'e':
                dir = 3
            elif d == 's':
                dir = 1
            else:
                dir = 2

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            cr, cc = place[i]

            q = deque()
            q.append([cr,cc])

            while q:
                cr, cc = q.popleft()
                nr = cr + dr[dir]
                nc = cc + dc[dir]

                if 0 <= nr < N and 0 <= nc < M and (room_copy[nr][nc] == 0 or room_copy[nr][nc] == '#'):
                    q.append([nr, nc])
                    room_copy[nr][nc] = '#'
                elif 0 <= nr < N and 0 <= nc < M and (room_copy[nr][nc] != 6):
                    q.append([nr, nc])
                else:
                    break

    cnt = 0
    flag = 0
    for r in range(N):
        for c in range(M):
            if room_copy[r][c] == 0:
                cnt += 1
                if cnt > minimum:
                    flag = 1
                    break
        if flag == 1:
            break

    if cnt < minimum:
        minimum = cnt
        # print(room_copy)

    # print(room_copy)
    # print(cnt)

print(minimum)
