import sys
input = sys.stdin.readline

N = int(input())
dungchi = [list(map(int, input().split(' '))) for _ in range(N)]

for i in dungchi:
    current = i
    cnt = 0
    for j in dungchi:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt+1, end=' ')