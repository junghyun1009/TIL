from collections import deque

puyo = [list(input()) for _ in range(12)]
rlt = 0

# 1. 터질 것이 있는지 확인
def check(color, r, c):
    global tmp, visited

    q = deque()
    q.append([r, c])
    tmp.append([r, c])
    visited[r][c] = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < 12 and 0 <= nc < 6 and puyo[nr][nc] == color and visited[nr][nc] == 0:
                q.append([nr, nc])
                tmp.append([nr, nc])
                visited[nr][nc] = 1

while True:
    visited = [[0] * 6 for _ in range(12)]
    target = []
    # print(puyo)
    
    for row in range(12):
        for col in range(6):
            if puyo[row][col] != '.' and visited[row][col] == 0:
                tmp = []
                check(puyo[row][col], row, col)
                if len(tmp) >= 4:
                    for t in tmp:
                        target.append(t)

    # print(target)
    if len(target) == 0:
        break

    # 2. 터뜨린 후 아래로 이동
    for each in target:
        puyo[each[0]][each[1]] = '.'

    # 2-1. 세로줄 확인하면서 빈칸 개수 세기
    blank = [0] * 6
    for row in range(12):
        for col in range(6):
            if puyo[row][col] == '.':
                blank[col] += 1

    # 2-2. 세로줄 확인하면서 빈칸이 아닌 알파벳 저장하기
    for col in range(6):
        word = []
        for row in range(12):
            if puyo[row][col] != '.':
                word.append(puyo[row][col])
        for b in range(blank[col]):
            puyo[b][col] = '.'
        for w in range(len(word)):
            puyo[blank[col]+w][col] = word[w]

    rlt += 1
    
print(rlt)
