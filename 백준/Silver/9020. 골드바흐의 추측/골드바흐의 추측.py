def check(a):

    cnt = 0
    for i in range(1, a // 2 + 1):
        if a % i == 0:
           cnt += 1

    if cnt == 1:
        return True
    else:
        return False


T = int(input())

for tc in range(T):
    n = int(input())

    for i in range(n // 2, 0, -1):
        if check(i) and check(n-i):
            print(i, end=' ')
            print(n - i)
            break