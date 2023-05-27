from collections import deque

def bfs(sr, sc):
    q = deque()
    q.append([sr, sc])
    cheeze[sr][sc] = 2
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while q:
        cr, cc = q.popleft()
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if 0 <= nr < N and 0 <= nc < M and cheeze[nr][nc] == 0:
                q.append([nr, nc])
                cheeze[nr][nc] = 2

            
N, M = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(N)]

melting = [arr[:] for arr in cheeze]
cheeze_sum = 0
for r in range(N):
    for c in range(M):
        cheeze_sum += cheeze[r][c]
time = 0

while True:
    if cheeze_sum == 0:
        print(time)
        break

    time += 1
    
    # 1. 외부 공기 2로 바꾸기
    bfs(0, 0)
    # print(cheeze)

    # 2. 치즈가 외부 공기와 접촉해있는 면 개수 세기
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for row in range(N):
        for col in range(M):
            if cheeze[row][col] == 1:
                air = 0
                for d in range(4):
                    nr = row + dr[d]
                    nc = col + dc[d]

                    if (0 <= nr < N) and (0 <= nc < M) and cheeze[nr][nc] == 2:
                        air += 1

                if air >= 2:
                    melting[row][col] = 0

    # 3. 녹은 치즈 배열 복사
    cheeze = [arr[:] for arr in melting]
    # print(cheeze)
    cheeze_sum = 0
    for r in range(N):
        for c in range(M):
            cheeze_sum += cheeze[r][c]

                
