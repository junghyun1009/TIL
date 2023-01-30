T = int(input())

for tc in range(1, T + 1):
    k = int(input())
    n = int(input())

    apt = [[0] * (n+1) for _ in range(k+1)]
    # print(apt)

    # 0층 먼저
    for i in range(1, n+1):
        apt[0][i] = i
    # print(apt)

    # 1층 이상
    for j in range(1, k+1):
        for m in range(1, n+1):
            for l in range(1, m+1):
                apt[j][m] += apt[j-1][l]

    print(apt[k][n])