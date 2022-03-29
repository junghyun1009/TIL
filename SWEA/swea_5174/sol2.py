import sys

sys.stdin = open('input.txt')


def bfs(s):

    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.pop(0)

        for i in range(E+2):
           if tree[x][i] == 1 and visited[i] == 0:
               queue.append(i)
               visited[i] = 1

    return sum(visited)


T = int(input())

for tc in range(1, T + 1):

    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    rel = []
    for i in range(0, 2 * E, 2):
        rel.append([node[i], node[i+1]])

    # print(rel)
    tree = [[0] * (E+2) for _ in range(E+2)]
    visited = [0] * (E+2)

    for i in rel:
        tree[i[0]][i[1]] = 1

    print(f'#{tc} {bfs(N)}')

