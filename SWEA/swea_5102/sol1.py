import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

def bfs(start, end):

    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt = 0
    rlt = []

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

                if i == end:
                    cnt += 1
                    rlt.append(cnt)

        cnt += 1

    return rlt

for tc in range(1, T + 1):

    v, e = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    graph = [[] for _ in range(v + 1)]

    for i in a:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    visited = [False] * (v + 1)

    print(graph)

    print(f'#{tc} {bfs(s, g)}')

