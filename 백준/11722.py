n = int(input())
a = list(map(int, input().split()))

dp = [[1, 0] for _ in range(n+1)]

for i in range(2, n+1):
    if a[i-2] <= a[i-1] and dp[i-1] > 1:
        dp[i] = dp[i-1] - 1

    elif a[i-2] <= a[i-1] and dp[i-1] <= 1:
        dp[i] = dp[i-1]

    else:
        dp[i] = dp[i-1] + 1

print(dp)