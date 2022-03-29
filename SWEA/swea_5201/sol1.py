import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())        # N:화물 수, M:트럭 수
    W = list(map(int, input().split()))     # 화물 무게
    T = list(map(int, input().split()))     # 트럭 적재용량

    move = 0        # 적재 가능 최대 용량을 계산할 변수
    cnt = 0         # 검토 횟수를 계산할 변수
    W = sorted(W)       # 화물이 가벼운 순서로 나열
    T = sorted(T)[::-1]       # 많이 적재할 수 있는 순서로 나열
    x = min(N, M)       # 화물 수와 트럭 수 중 작은 수만큼 적재 가능
    t = 0       # 트럭 인덱스

    while True:
        if cnt == x:        # 검토 횟수를 만족하면 중단
            break

        w = W.pop()     # 화물에서 하나씩 꺼내면서 확인
        if T[t] >= w:       # 트럭의 적재 가능용량이 화물보다 크다면
            move += w       # 적재
            t += 1      # 다음 트럭
        cnt += 1        # 검토 횟수 1 증가

    print(f'#{tc} {move}')

