import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
x = int(input())

A.sort()
add = 0
cnt = 0

for start in range(n):
    add = A[start]
    if add >= x:
        break
    end = start + 1
    
    while end < n:
        add += A[end]
        
        if add == x:
            cnt += 1
        elif add > x:
            break

        add -= A[end]
        end += 1

    add = 0

print(cnt)