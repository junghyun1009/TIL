import sys
input = sys.stdin.readline

R, C, T = map(int, input().split(' '))
room = [list(map(int, input().split(' '))) for _ in range(R)]

for _ in range(T):

    room_copy = [arr[:] for arr in room]

    # 공기청정기, 미세먼지 위치 파악
    fresh = []
    dust = []
    for r in range(R):
        for c in range(C):
            if room[r][c] == -1:
                fresh.append([r, c])
            elif room[r][c] != 0:
                dust.append([r, c])

    # 미세먼지 이동
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for cr in range(R):
        for cc in range(C):
            if room[cr][cc] != -1:
                cnt = 0
                for dir in range(4):
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]

                    if 0 <= nr < R and 0 <= nc < C and room_copy[nr][nc] != -1:
                        room[cr][cc] = room[cr][cc] + int(room_copy[nr][nc]/5)
                        cnt += 1

                room[cr][cc] -= int(room_copy[cr][cc]/5) * cnt
    
    # print('!')
    # print(room)
    
    # 공기청정기 가동
    # 위쪽 공기청정기는 반시계
    upper = fresh[0]
    # 남
    corner_a = room[upper[0]][C-1]
    for a in range(C-1, 1, -1):
        room[upper[0]][a] = room[upper[0]][a-1]
    room[upper[0]][1] = 0
    # 동
    corner_b = room[0][C-1]
    for b in range(0, upper[0]-1):
        room[b][C-1] = room[b+1][C-1]
    room[upper[0]-1][C-1] = corner_a
    #북
    corner_c = room[0][0]
    for c in range(0, C-1):
        room[0][c] = room[0][c+1]
    room[0][C-2] = corner_b
    # 서
    for d in range(upper[0]-1, 1, -1):
        room[d][0] = room[d-1][0]
    room[1][0] = corner_c

    # print('!!')
    # print(room)
    
    # 아래쪽 공기청정기는 시계
    down = fresh[1]
    # 북
    corner_a = room[down[0]][C-1]
    for a in range(C-1, 1, -1):
        room[down[0]][a] = room[down[0]][a-1]
    room[down[0]][1] = 0
    # 동
    corner_b = room[R-1][C-1]
    for b in range(R-1, down[0]+1, -1):
        room[b][C-1] = room[b-1][C-1]
    room[down[0]+1][C-1] = corner_a
    #남
    corner_c = room[R-1][0]
    for c in range(0, C-1):
        room[R-1][c] = room[R-1][c+1]
    room[R-1][C-2] = corner_b
    # 서
    for d in range(down[0]+1, R-2):
        room[d][0] = room[d+1][0]
    room[R-2][0] = corner_c

    # print('!!!')
    # print(room)

ans = 0
for r in room:
    for c in r:
        if c != -1:
            ans += c

print(ans)
