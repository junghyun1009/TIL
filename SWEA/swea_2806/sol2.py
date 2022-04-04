import sys

sys.stdin = open('input.txt')


def DFS_1(n):
    global ans

    if n == N:
        ans += 1
        return

    for j in range(N):
        # 현재 위치 n, j 기준으로 규칙성 파악
        if v1[j] == v2[n + j] == v3[n - j] == 0:
            v1[j] = v2[n + j] = v3[n - j] = 1
            DFS_1(n+1)
            v1[j] = v2[n + j] = v3[n - j] = 0


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    ans = 0
    v1, v2, v3 = [0] * 30, [0] * 30, [0] * 30
    # 위쪽 방향 방문, 왼쪽 대각선 방문, 오른쪽 대각선 방문 표시
    DFS_1(0)

    print(f'#{tc} {ans}')

