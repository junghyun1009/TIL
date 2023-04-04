import sys
input = sys.stdin.readline

N, M = map(int, input().split(' '))
num = [list(map(int, input().split(' '))) for _ in range(N)]

# print(num)
visited = [[0] * M for _ in range(N)]
maxsum = 0
maxlist = []

def dfs(arr, cr, cc):
    global maxsum, maxlist
    
    if len(arr) == 4:
        # print(arr)
        if maxsum < sum(arr):
            maxsum = sum(arr)
            maxlist = arr
        return
    # visited[cr][cc] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for d in range(4):
        nr = cr + dr[d]
        nc = cc + dc[d]

        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            dfs(arr+[num[nr][nc]], nr, nc)
            visited[nr][nc] = 0

for r in range(N):
    for c in range(M):
        visited[r][c] = 1
        dfs([], r, c)
        visited[r][c] = 0
        
# print(maxsum)
# print(maxlist)

# ㅏ ㅓ
for c in range(M):
    for r in range(0, N-2):
        hor = num[r][c] + num[r+1][c] + num[r+2][c]
        if c == 0:
            tmp = hor + num[r+1][c+1]
        elif c == M - 1:
            tmp = hor + num[r+1][c-1]         
        else:
            left = hor + num[r+1][c-1]
            right = hor + num[r+1][c+1]
            tmp = max(left, right)

        if maxsum < tmp:
            maxsum = tmp

# ㅗ ㅜ
for j in range(N):
    for k in range(0, M-2):
        row = num[j][k] + num[j][k+1] + num[j][k+2]
        if j == 0:
            tmpp = row + num[j+1][k+1]
        elif j == N - 1:
            tmpp = row + num[j-1][k+1]
        else:
            up = row + num[j-1][k+1]
            down = row + num[j+1][k+1]
            tmpp = max(up, down)

        if maxsum < tmpp:
            maxsum = tmpp

print(maxsum)    
