# 제출용
import sys

sys.stdin = open('input.txt')


# 모든 부분집합에서 최대 수익 구하는 함수
def subset(s, ssum):
    global money

    if s == M + 1:
        return

    if money < ssum:
        money = ssum

    for i in range(s, M):
        if i not in tmp and sum(k) + each[i] <= C:
            tmp.append(i)
            k.append(each[i])
            ssum += each[i] ** 2
            subset(i + 1, ssum)
            ssum -= each[i] ** 2
            tmp.pop()
            k.pop()


T = int(input())

for tc in range(1, T + 1):

    N, M, C = map(int, input().split())  # N:벌통 크기, M:벌통 개수, C:꿀 채취 최대 양
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 수익, 시작 행, 열 저장
    profit = []
    for r in range(N):
        for c in range(N - (M - 1)):
            each = honey[r][c:c + M]
            tmp = []
            k = []
            money = 0
            ssum = 0
            subset(0, ssum)
            profit.append([money, r, c])

    profit.sort(key=lambda x: x[0])
    cnt = 0

    while True:
        if cnt == 2:
            break

        check = profit.pop()

        # 일꾼1
        if cnt == 0:
            earn = check[0]
            row = check[1]
            scol = check[2]
            ecol = check[2] + M - 1
            cnt += 1

        # 일꾼2
        elif cnt == 1:
            # 행이 다른 경우
            if row != check[1]:
                earn += check[0]
                cnt += 1

            # 행이 같은 경우
            else:
                # 범위가 겹치지 않는 경우
                if check[2] > ecol or check[2] + M - 1 < scol:
                    earn += check[0]
                    cnt += 1

    print(f'#{tc} {earn}')

