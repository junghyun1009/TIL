n = int(input())

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1, n+1):
    for j in range(0, i):
        dp[i] += dp[j] * dp[i-1-j]

print(dp[n])

# for i in range(2, n+1):
#     rlt = 0
#     for j in range(0, n):
#         tmp = [j, n-1-j]
#         rlt += dp[tmp[0]] * dp[tmp[1]]
#     dp.append(rlt)
#     print(dp)

# print(dp[n])