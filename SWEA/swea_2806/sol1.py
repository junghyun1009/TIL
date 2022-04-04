import sys

sys.stdin = open('input.txt')


def check(si, sj):      # 퀸을 놓을 수 있는 자리인지 확인
    # 1. 위쪽 방향
    for i in range(si - 1, -1, -1):
        if v[i][sj] == 1:       # 퀸을 만나면 실패
            return 0

    # 2. 왼쪽 대각선 위
    i, j = si - 1, sj - 1
    while i >= 0 and j >= 0:
        if v[i][j] == 1:
            return 0
        i, j = i - 1, j - 1

    # 3. 오른쪽 대각선 위
    i, j = si - 1, sj + 1
    while i >= 0 and j < N:
        if v[i][j] == 1:
            return 0
        i, j = i - 1, j + 1

    # 세 방향 모두 퀸 없음!
    return 1


def DFS(n):
    global ans

    if n == N:
        ans += 1
        return

    for j in range(N):
        if check(n, j):     # 퀸을 놓을 수 있다면
            v[n][j] = 1
            DFS(n+1)
            v[n][j] = 0


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    v = [[0] * N for _ in range(N)]
    ans = 0
    DFS(0)

    print(f'#{tc} {ans}')

