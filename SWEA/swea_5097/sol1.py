import sys
from collections import deque

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))

    queue = deque()
    for i in numbers:
        queue.append(i)

    for j in range(m):
        a = queue.popleft()
        queue.append(a)
    
    print(f'#{tc} {queue[0]}')

