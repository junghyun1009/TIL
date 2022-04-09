import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(a):
    cnt = 0
    Q = deque()
    for i in a:
        Q.append(i)
        visited[i[0]][i[1]][i[2]] = 1

    # 위 아래 왼쪽 오른쪽 앞 뒤
    dh = [-1, 1, 0, 0, 0, 0]
    dn = [0, 0, 0, 0, -1, 1]
    dm = [0, 0, -1, 1, 0, 0]

    while Q:
        ch, cn, cm = Q.popleft()

        for dir in range(6):
            nh = ch + dh[dir]
            nn = cn + dn[dir]
            nm = cm + dm[dir]

            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and tomato[nh][nn][nm] == 0 and visited[nh][nn][nm] == 0:
                Q.append([nh, nn, nm])
                visited[nh][nn][nm] = visited[ch][cn][cm] + 1
                cnt += 1

        if len(Q) == 0:
            return visited[ch][cn][cm] - 1, cnt


M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

one = []
zero = 0

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                one.append([h, n, m])
            elif tomato[h][n][m] == 0:
                zero += 1

if zero == 0:
    rlt = 0
elif len(one) == 0:
    rlt = -1
else:
    rlt, rite = bfs(one)
    if rite != zero:
        rlt = -1

print(rlt)
