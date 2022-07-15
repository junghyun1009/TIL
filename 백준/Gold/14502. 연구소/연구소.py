import sys
from collections import deque

input = sys.stdin.readline
    

def dfs(s, tmp):
    global min_cnt

    if len(tmp) == 3:
        visited_lab = [[0] * M for _ in range(N)]

        def bfs(sr, sc):

            queue = deque()
            queue.append([sr, sc])
            visited_lab[sr][sc] = 1
            cnt = 0

            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            while queue:
                r, c = queue.popleft()

                for dir in range(4):
                    nr = r + dr[dir]
                    nc = c + dc[dir]

                    if 0 <= nr < N and 0 <= nc < M and lab[nr][nc] == 0 and visited_lab[nr][nc] == 0:
                        queue.append([nr, nc])
                        visited_lab[nr][nc] = 1
                        cnt += 1

            return cnt

        # bfs 돌려서 안전영역 확인
        rlt = 0
        for j in virus:
            rlt += bfs(j[0], j[1])

        if rlt < min_cnt:
            min_cnt = rlt
        
        return

    for i in range(s, len(blank)):
        if visited[i] == 0:
            visited[i] = 1
            # 벽 세우기
            lab[blank[i][0]][blank[i][1]] = 1
            dfs(i+1, tmp + [blank[i]])
            lab[blank[i][0]][blank[i][1]] = 0
            visited[i] = 0


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# print(N)
# print(M)
# pprint(lab)

blank = []
virus = []

for r in range(N):
    for c in range(M):
        if lab[r][c] == 0:
            blank.append([r, c])
        elif lab[r][c] == 2:
            virus.append([r, c])

visited = [0] * len(blank)
min_cnt = 9999999
dfs(0, [])
print(len(blank) - min_cnt - 3)
