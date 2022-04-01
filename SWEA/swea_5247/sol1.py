from collections import deque


def bfs(s, e):

    Q = deque()
    Q.append(s)
    visited[s] = 1

    while Q:
        now = Q.popleft()
        if now == e:
            return visited[now] - 1

        for i in range(4):
            if i == 0:
                x = now + 1
                if 0 < x <= 1000000 and visited[x] == 0:
                    Q.append(x)
                    visited[x] = visited[now] + 1

            elif i == 1:
                x = now - 1
                if 0 < x <= 1000000 and visited[x] == 0:
                    Q.append(x)
                    visited[x] = visited[now] + 1

            elif i == 2:
                x = now * 2
                if 0 < x <= 1000000 and visited[x] == 0:
                    Q.append(x)
                    visited[x] = visited[now] + 1

            else:
                x = now - 10
                if 0 < x <= 1000000 and visited[x] == 0:
                    Q.append(x)
                    visited[x] = visited[now] + 1


T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    visited = [0] * 1000001
    
    print(f'#{tc} {bfs(N, M)}')

