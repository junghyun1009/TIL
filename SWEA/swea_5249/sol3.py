import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs():
    global cnt

    Q = deque()
    for t in tree:
        Q.append(t)

    a, b, c = Q.popleft()
    check[a] += 1
    check[b] += 1
    cnt += c

    while Q:
        r, c, w = Q.popleft()

        if check[r] == 0 or check[c] == 0:
            check[r] += 1
            check[c] += 1
            cnt += w


T = int(input())

for tc in range(1, T + 1):

    V, E = map(int, input().split())
    tree = [list(map(int, input().split())) for _ in range(E)]

    tree.sort(key=lambda x: x[2])

    check = [0] * (V + 1)

    cnt = 0
    bfs()

    print(f'#{tc} {cnt}')