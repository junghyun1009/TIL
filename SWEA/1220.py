for tc in range(1):

    n = int(input())

    a = [list(map(int, input().split())) for _ in range(n)]

    # 1은 아래로 내려가고 2는 위로 올라가야 함
    cnt = 0

    for c in range(n):
        for r in range(n):
            if a[c][r] == 1:
                find = r
                for i in range(r+1, n):
                    if a[c][i] == 1:
                        break

                    elif a[c][i] == 2:
                        cnt += 1

    print(cnt)