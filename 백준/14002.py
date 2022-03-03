# n = int(input())
# a = list(map(int, input().split()))
#
# dp = [[1, 0] for _ in range(n)]
#
# for i in range(1, n):
#     for j in range(i):
#         if a[j] < a[i]:
#             dp[i][0] = max(dp[i][0], dp[j][0] + 1)
#             if dp[i][0] == dp[j][0] + 1:
#                 dp[i][1] = j

# print(dp)
# print(max(dp)[0])
# rlt = max(dp)[0]
# for i in range(1, rlt+1):
#     for j in range(n):
#         if dp[j][0] == i:
#             print(a[dp[j][1]], end=' ')

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