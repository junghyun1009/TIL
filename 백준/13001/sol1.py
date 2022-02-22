# T = int(input())
#
# for tc in range(1, T + 1):

n = int(input())

dp_a = [0 for _ in range(n+1)]

dp_a[0] = 0
dp_a[1] = 1

for i in range(2, n+1):
    dp_a[i] += dp_a[i-2] + dp_a[i-1]

dp_b = [0 for _ in range(n+1)]

dp_b[0] = 0
dp_b[1] = 4

for j in range(2, n+1):
    dp_b[j] += dp_b[j-1] - dp_a[j] + dp_a[j] * 3

print(f'{dp_b[n]}')

