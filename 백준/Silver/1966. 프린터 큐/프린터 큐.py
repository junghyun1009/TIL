T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    star = list(map(int, input().split()))

    cnt = 1

    while True:
        if (M == 0 and max(star) == star[0]):
            break
        if star[0] != max(star):
            top = star.pop(0)
            star.append(top)
            if M == 0:
                M = len(star) - 1
            else:
                M -= 1
        else:
            star.pop(0)
            cnt += 1
            M -= 1

    print(cnt)