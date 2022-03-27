import sys

sys.stdin = open('input.txt')


def bfs(s):

    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.pop(0)

        for i in range(V+1):
            if graph[x][i] == 1 and visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1

                if i == G:
                    return visited[i] - 1

    return 0


T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    graph = [[0] * (V+1) for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in a:
        graph[i[0]][i[1]] = 1
        graph[i[1]][i[0]] = 1
    
    print(f'#{tc} {bfs(S)}')

