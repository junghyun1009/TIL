import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    t = [[0] * n for _ in range(n)]
    cnt_max = []
    cost = []

    # 마름모의 중앙과 인덱스를 맞춰준다고 생각
    for k in range(1, 2*n):
        cnt_list = []
        for i in range(n):
            for j in range(n):
                cnt = 0
                # t[i][j-(k-1):j+k] = [1] * (2 * k + 1)
                # for l in range(1, k):
                #     if 0 <= i-(k-l) < n and 0 <= i+(k-l) < n:
                #         t[i-(k-l)][j-(l-1):j+l] = [1] * (2 * l - 1)
                #         t[i+(k-l)][j-(l-1):j+l] = [1] * (2 * l - 1)

                for q in range(j-(k-1), j+k):
                    if 0 <= q < n:
                        if a[i][q] == 1:
                            cnt += 1

                for l in range(1, k):
                    for r in range(j-(l-1), j+l):
                        if 0 <= i-(k-l) < n and 0 <= r < n:
                            if a[i-(k-l)][r] == 1:
                                cnt += 1
                            # if a[i+(k-l)][r] == 1:
                            #     cnt += 1
                        if 0 <= i+(k-l) < n and 0 <= r < n:
                            if a[i+(k-l)][r] == 1:
                                cnt += 1
                # if t[i][j] == a[i][j]:
                #     cnt += 1
                # cnt_list.append(cnt)
                cnt_list.append(cnt)
        cnt_max.append([k, max(cnt_list)])

    for i in cnt_max:
        manage = i[0]**2 + (i[0]-1)**2
        earn = i[1] * m
        if earn - manage >= 0:
            cost.append(i[1])

    # print(cnt_list)
    # print(cnt_max)
    # print(cost)
    print(f'#{tc} {max(cost)}')

