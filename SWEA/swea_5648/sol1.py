import sys

sys.stdin = open('input.txt')


def bfs():

    queue = []
    for a in atom:
        queue.append([a[0], a[1]])

    while queue:




T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    atom = [list(map(int, input().split())) for _ in range(N)]

    for a in atom:
        a[0] += 1000
        a[1] = 1000 - a[1]

    
    print(f'#{tc} ')

