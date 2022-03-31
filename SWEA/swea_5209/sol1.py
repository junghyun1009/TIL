import sys

sys.stdin = open('input.txt')


def dfs(ssum):      # 생산 최소 비용 계산 함수(구한 순열대로 각 공장이 순서대로 가져가게 함)
    global cnt, msum

    if cnt == N - 1:        # 공장의 수만큼 셌다면 최솟값 갱신
        if msum > ssum:
            msum = ssum
            return

    if msum < ssum:     # 지금까지 계산한 ssum이 이미 최솟값보다 크다면 중단
        return

    for i in range(N):
        if visited[i] == 0:     # 방문하지 않았다면
            visited[i] = 1      # 방문 표시
            cnt += 1        # 횟수 추가
            dfs(ssum + V[cnt][i])       # 해당 공장에서의 생산 비용 더해서 넘겨줌
            visited[i] = 0      # 복원
            cnt -= 1


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    cnt = -1
    msum = 99999
    ssum = 0

    dfs(ssum)
    
    print(f'#{tc} {msum}')

