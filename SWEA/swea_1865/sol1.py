import sys

sys.stdin = open('input.txt')


def dfs(p):     # 최대 확률을 구하는 함수
    global cnt, maxp

    if cnt == N - 1:        # 일의 개수를 모두 채웠으면
        if maxp < p:        # 최대 확률 갱신
            maxp = p
            return

    if p <= maxp:       # 지금까지 계산한 확률이 최대 확률보다 이미 작거나 같다면 중단
        return

    for i in range(N):
        if visited[i] == 0:     # 아직 방문하지 않았다면
            visited[i] = 1      # 방문 처리하고
            cnt += 1        # 횟수 추가해주기
            dfs(p * (P[cnt][i] / 100))      # 현재 받아온 확률에 새로운 확률 곱해주기
            visited[i] = 0      # 복원
            cnt -= 1


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    cnt = -1
    maxp = 0
    dfs(1)
    rlt = maxp * 100
    
    print(f'#{tc} {rlt:.6f}')

