# from itertools import combinations

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    a = 1
    for i in range(1, M + 1):
        a *= i

    b = 1
    for i in range(1, N + 1):
        b *= i

    c = 1
    for i in range(1, M - N + 1):
        c *= i

    rlt = int(a / (b * c))
    print(rlt)