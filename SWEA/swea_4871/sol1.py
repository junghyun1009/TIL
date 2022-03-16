import sys

sys.stdin = open('input.txt')

def dfs(start, end):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            if i == end:
                return 1
            else:
                return dfs(i, end)

    else:
        return 0


T = int(input())

for tc in range(1, T + 1):

    v, e = map(int, input().split())
    line = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    graph = [[] for _ in range(v+1)]

    for i in line:
        graph[i[0]].append(i[1])

    visited = [False] * (v+1)

    print(f'#{tc} {dfs(s, g)}')

