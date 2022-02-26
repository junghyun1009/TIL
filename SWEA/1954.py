T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    snail = [[0] * n for _ in range(n)]

    # 우 하 좌 상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = 0
    c = 0
    d = 0
    snail[r][c] = 1

    for i in range(2, n**2+1):
        r = r + dr[d]
        c = c + dc[d]

        if 0 <= r < n and 0 <= c < n and snail[r][c] == 0:
            snail[r][c] = i

        else:
            r = r - dr[d]
            c = c - dc[d]
            d = (d + 1) % 4
            r = r + dr[d]
            c = c + dc[d]
            snail[r][c] = i

    print(f'#{tc}')
    for a in snail:
        print(*a)



