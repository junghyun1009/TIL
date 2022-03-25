def dfs(s):
    if len(lotto) == 6:
        print(*lotto)
        return

    for i in range(s, num):
        if numbers[i] not in lotto:
            lotto.append(numbers[i])
            dfs(i+1)
            lotto.pop()


while True:
    pick = list(map(int, input().split()))
    # print(pick)
    if pick[0] == 0:
        break

    num = pick[0]
    numbers = pick[1:]
    lotto = []
    dfs(0)
    print()