a = [1, 3, 1, 5, 101, 100]

dp = [0] * len(a)
dp[0] = 1
dp[1] = 3
for i in range(2, len(a)):
    dp[i] = max(dp[i-2]+a[i], dp[i-1])

print(max(dp))