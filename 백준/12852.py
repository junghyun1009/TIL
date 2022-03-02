n = int(input())

dp = [0] * 1000001

for i in range(2, n + 1):

    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)

print(dp[n])

cnt = 0
i = n
cal = [i]

while True:

    dp[i] = dp[i-1] + 1

    if i == 1:
        break

    if (i % 3 != 0) and (i % 2 != 0):
        cal.append(i-1)
        i = i - 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
        if dp[i] == dp[i-1] + 1:
            cal.append(i-1)
            i = i - 1
        else:
            cal.append(i//3)
            i = i // 3

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        if dp[i] == dp[i-1] + 1:
            cal.append(i - 1)
            i = i - 1
        else:
            cal.append(i//2)
            i = i // 2

print(*cal)