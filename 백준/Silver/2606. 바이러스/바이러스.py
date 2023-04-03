from collections import deque

N = int(input())
P = int(input())
pair = [list(map(int, input().split(' '))) for _ in range(P)]

net = [[] for _ in range(N+1)]
for i in pair:
    net[i[0]].append(i[1])
    net[i[1]].append(i[0])

q = deque()
visited = [0] * (N+1)
visited[1] = 1
for j in net[1]:
    q.append(j)
    visited[j] = 1

while q:
    cur = q.popleft()
    for k in net[cur]:
        if visited[k] == 0:
            q.append(k)
    visited[cur] = 1

print(sum(visited)-1)