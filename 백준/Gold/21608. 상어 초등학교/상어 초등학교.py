N = int(input())
student = [list(map(int, input().split())) for _ in range(N**2)]
order_student = sorted(student)
seat = [[0] * N for _ in range(N)]
# print(student)
# print(seat)

# 1. 각 자리마다 인접한 자리에 좋아하는 학생이 몇 명 있는지 세기
# 2. 각 자리마다 인접한 자리에 빈칸이 몇 개 있는지 세기
# 3. 행의 번호가 가장 작은 칸
# 4. 열의 번호가 가장 작은 칸

for num in student:
    tmp = []
    cur_student = num[0]
    like_student = num[1:]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for r in range(N):
        for c in range(N):
            if seat[r][c] == 0:
                like_cnt = 0
                blank_cnt = 0
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < N and 0 <= nc < N:
                        if seat[nr][nc] in like_student:
                            like_cnt += 1
                        elif seat[nr][nc] == 0:
                            blank_cnt += 1
                tmp.append([like_cnt, blank_cnt, r, c])
    order = sorted(tmp, key = lambda x: (-x[0], -x[1], x[2], x[3]))
    # print(order)
    seat[order[0][2]][order[0][3]] = cur_student

# print(seat)
score = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for r in range(N):
    for c in range(N):
        cur_student = seat[r][c]
        like_student = order_student[cur_student-1][1:]
        like_cnt = 0
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < N and  seat[nr][nc] in like_student:
                like_cnt += 1
        if like_cnt > 0:
            score += (10**(like_cnt-1))

print(score)
    
