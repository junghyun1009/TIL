def dfs(s, tmp):
    if len(tmp) == 3:
        flag = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        for t in teacher:
            r = t[0]
            c = t[1]
            for dir in range(4):
                for p in range(1, N):
                    nr = r + dr[dir] * p
                    nc = c + dc[dir] * p
                    if 0 <= nr < N and 0 <= nc < N:
                        if hall[nr][nc] == 'O':
                            break
                        elif hall[nr][nc] == 'S':
                            return                   
        
        flag = 1
        return flag
    
    for i in range(s, len(can)):
        if visited[i] == 0:
            visited[i] = 1
            hall[can[i][0]][can[i][1]] = 'O'
            a = dfs(i+1, tmp + [can[i]])
            if a == 1:
                return 1
            visited[i] = 0
            hall[can[i][0]][can[i][1]] = 'P'
            
        

N = int(input())
hall = [list(input().split()) for _ in range(N)]

teacher_row = []
teacher_col = []
teacher = []
can = []

for i in range(N):
    for j in range(N):
        if hall[i][j] == 'T':
            teacher_row.append(i)
            teacher_col.append(j)
            teacher.append([i, j])

for r in teacher_row:
    for c in range(N):
        if hall[r][c] == 'X':
            hall[r][c] = 'P'

for c in teacher_col:
    for r in range(N):
        if hall[r][c] == 'X':
            hall[r][c] = 'P'

for r in range(N):
    for c in range(N):
        if hall[r][c] == 'P':
            can.append([r, c])

visited = [0 for _ in range(len(can))]
rlt = dfs(0, [])
if rlt == 1:
    print('YES')
else:
    print('NO')
