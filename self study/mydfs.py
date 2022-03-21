# swea_4871

def dfs(s, g):
    stack = []
    stack.append(s)
    visited[s] = 1

    while stack:
        now = stack[-1]
        for i in range(1, v + 1):
            if graph[now][i] == 1 and visited[i] == 0:
                if i == g:
                    return 1
                else:
                    stack.append(i)
                    visited[i] = 1
                    break
        else:
            stack.pop()

    return 0


T = int(input())

for tc in range(1, T + 1):

    v, e = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(e)]
    s, g = map(int, input().split())

    graph = [[0] * (v + 1) for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for i in a:
        graph[i[0]][i[1]] = 1

    print(f'#{tc} {dfs(s, g)}')

