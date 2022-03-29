a, b = map(int, input().split())
cnt = 1

while True:
    if b == a:
        break

    elif (b % 2 != 0 and b % 10 != 1) or b < a:
        cnt = -1
        break

    if b % 2 == 0:
        b = b // 2
        cnt += 1

    else:
        b = b - 1
        b = b // 10
        cnt += 1

print(cnt)