import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

end = 0
add = 0
cnt = 0

for start in range(N):
    while add < M and end < N:
        add += A[end]
        end += 1
    if add == M:
        cnt += 1
    add -= A[start]

print(cnt)
        
        
    
