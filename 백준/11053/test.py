# N = int(input())
#
# A = list(map(int, input().split()))
#
# dp = [1] * N
#
# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             dp[i] = max(dp[i],dp[j]+1)
#             print(j, i, dp[i])

n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(dp)
print(max(dp))