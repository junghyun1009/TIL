# 연습용
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
        if i not in tmp and sum(k)+each[i] <= C:
            tmp.append(i)
            k.append(each[i])
            ssum += each[i] ** 2
            subset(i+1, ssum)
            ssum -= each[i] ** 2
            tmp.pop()
            k.pop()


T = int(input())

for tc in range(1, T + 1):

    N, M, C = map(int, input().split())     # N:벌통 크기, M:벌통 개수, C:꿀 채취 최대 양
    honey = [list(map(int, input().split())) for _ in range(N)]

    # 총 꿀 양, 수익 저장
    profit = []
    for r in range(N):
        for c in range(N-(M-1)):
            each = honey[r][c:c+M]
            tmp = []
            k = []
            box = 0
            money = 0
            ssum = 0
            subset(0, ssum)
            profit.append([box, money, r, c])

    # print(profit)
    profit.sort(key=lambda x:x[1])
    # print(profit)
    cnt = 0
    
    while True:
        if cnt == 2:
            break
        
        check = profit.pop()
        # 꿀 채취 최대 양을 안 넘는 경우
        if check[0] <= C:
            if cnt == 0:
                earn = check[1]
                row = check[2]
                scol = check[3]
                ecol = check[3] + M - 1
                cnt += 1
            
            elif cnt == 1:
                # 행이 다른 경우
                if row != check[2]:
                    earn += check[1]
                    cnt += 1
                # 행이 같은 경우
                else:
                    # 범위가 겹치지 않는 경우
                    if check[3] > ecol or check[3] + M -1 < scol:
                        earn += check[1]
                        cnt += 1

    print(f'#{tc} {earn}')

