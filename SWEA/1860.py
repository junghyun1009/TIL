T = int(input())

for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))

    num = max(time) // m
    fish = []

    for i in range(num + 1):
        fish.append(i * k)

    for i in time:

        a = i // m

        if fish[a] == 0:
            rlt = 'Impossible'
            break

        else:
            for j in range(a, len(fish)):
                fish[j] -= 1

    else:
        rlt = 'Possible'

    print(f'#{tc} {rlt}')