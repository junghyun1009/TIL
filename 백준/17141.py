from pprint import pprint


def dfs(s, num):

    if len(sel) == m:
        tmp = sel[:]
        select.append(tmp)
        return

    for i in range(s, num):
        if i not in sel:
            sel.append(i)
            dfs(i+1, num)
            sel.pop()


def bfs():

    queue = []
    for i in tmp:
        queue.append(i)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and copy[nx][ny] == 0 and [nx, ny] not in tmp:
                copy[nx][ny] = copy[x][y] + 1
                queue.append([nx, ny])

    return copy[x][y]

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus = []
time_list = []

for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus.append([i, j])
            lab[i][j] = 0

        elif lab[i][j] == 1:
            lab[i][j] = '-'

# print(virus)
num = len(virus)
sel = []
select = []
dfs(0, num)
# print(select)
virus_list = []

for i in range(len(select)):
    tmp = []
    copy = [l[::] for l in lab]
    # print(copy)
    for j in range(m):
        tmp.append(virus[select[i][j]])

    for k in tmp:
        copy[k[0]][k[1]] = 0

    # print(tmp)
    # pprint(lab)
    time = bfs()

    cnt = 0
    for l in copy:
        for q in l:
            if q == 0:
                cnt += 1

    if cnt == m:
        time_list.append(time)
    # pprint(copy)

# print(time_list)

if len(time_list) == 0:
    rlt = -1
else:
    rlt = min(time_list)

print(rlt)