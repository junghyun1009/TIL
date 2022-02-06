t = int(input())
for tc in range(1, t+1):
    n = int(input())
#n = 32850

    money = {50000:0, 10000:0, 5000:0, 1000:0, 500:0, 100:0, 50:0, 10:0}

    for i in money:
        if n // i == 0:
            continue
        else:
            money[i] = n // i
            n = n % i

    print(f'#{tc}')
    for j in money:
        print(money[j], end=" ")
    print()

