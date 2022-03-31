def dfs(s, ssum):
    global cnt, msum

    if cnt == N:
        if msum < ssum:
            msum = ssum
            return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            cnt += 1
            dfs(i, ssum + abs(A[s]-A[i]))
            cnt -= 1
            visited[i] = 0


N = int(input())
A = list(map(int, input().split()))

visited = [0] * N
cnt = 1
msum = 0

for i in range(N):

    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0

print(msum)

