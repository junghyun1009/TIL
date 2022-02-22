n = int(input())

a = list(map(int, input().split()))

dp = [1 for _ in range(n)]
dp_a = a[:]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if dp_a[i] < a[j]:
            dp[i] += 1
            dp_a[i] = a[j]

print(dp)