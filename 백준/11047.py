N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

# print(coin)

cnt = 0
i = N - 1

while True:
    if K == 0:
        break

    if K >= coin[i]:
        K -= coin[i]
        cnt += 1

    else:
        i -= 1

print(cnt)