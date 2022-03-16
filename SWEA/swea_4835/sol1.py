import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    rlt = []

    for i in range(n - m + 1):
        sub = sum(a[i:i+m])
        rlt.append(sub)
    
    print(f'#{tc} {max(rlt)-min(rlt)}')

