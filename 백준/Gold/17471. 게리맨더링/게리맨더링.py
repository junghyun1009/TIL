from collections import deque

def bfs(s):
    global cnt

    Q = deque()
    Q.append(s)
    visited[s] = 1
    cnt += people[s]

    while Q:
        now = Q.popleft()

        for i in range(1, area[now][0] + 1):
            if visited[area[now][i]] == 0:
                Q.append(area[now][i])
                visited[area[now][i]] = 1
                cnt += people[area[now][i]]

    return cnt


def connect(s, num, a):

    Q = deque()
    Q.append(s)
    visited = [0] * (N + 1)
    visited[s] = 1
    tmp = 1

    while Q:
        now = Q.popleft()

        for i in range(1, area[now][0] + 1):
            if visited[area[now][i]] == 0 and area[now][i] in a:
                Q.append(area[now][i])
                visited[area[now][i]] = 1
                tmp += 1

    if tmp == num:
        return True
    else:
        return False


def dfs(s, tmp_a, people_a, num):
    global min_sub

    if len(tmp_a) == num and connect(tmp_a[0], num, tmp_a):
        tmp_b = []
        people_b = 0
        for i in range(1, N + 1):
            if visited[i] == 0:
                tmp_b.append(i)
                people_b += people[i]
        # print(tmp_a)
        # print(tmp_b)
        if connect(tmp_b[0], N - num, tmp_b):
            sub = abs(people_a - people_b)
            if min_sub > sub:
                min_sub = sub
            # print(sub)
            # print(min_sub)
            return min_sub

        return

    for i in range(s, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i+1, tmp_a + [i], people_a + people[i], num)
            visited[i] = 0


N = int(input())
people = [0] + list(map(int, input().split()))
area = [[0]] + [list(map(int, input().split())) for _ in range(N)]
# print(area)

visited = [0] * (N + 1)
# print(bfs(1))
group = []
rlt = 0

for i in range(1, N + 1):
    cnt = 0
    if visited[i] == 0:
        cnt = bfs(i)
        group.append(cnt)

# print(group)
min_sub = 99999

if len(group) > 2:
    rlt = -1
elif len(group) == 2:
    rlt = abs(group[0] - group[1])
else:
    for i in range(1, N):
        visited = [0] * (N + 1)
        dfs(1, [], 0, i)
        rlt = min_sub

print(rlt)