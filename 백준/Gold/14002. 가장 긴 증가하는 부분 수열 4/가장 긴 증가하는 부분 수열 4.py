n = int(input())
a = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

rlt = max(dp)
print(rlt)

b = []
# for i in range(rlt, 0, -1):
#     for j in range(n-1, -1, -1):
#         if dp[j] == i:
#             b.append(a[j])
#             break
idx = n - 1
while True:
    if rlt == 0:
        break

    if dp[idx] == rlt:
        b.append(a[idx])
        idx -= 1
        rlt -= 1

    else:
        idx -= 1

b = reversed(b)
print(*b)