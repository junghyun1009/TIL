import sys

sys.stdin = open('input.txt')


def dfs(sr, sc, ssum):      # 경로를 이동하며 자기 자리에 있는 숫자를 더해나가 최솟값을 찾는 함수
    global msum

    if sr < 0 or sr >= N or sc < 0 or sc >= N:      # 보드 밖으로 벗어나면 중단
        return

    elif sr == N - 1 and sc == N - 1:       # 도착지에 도달하면
        ssum += board[sr][sc]       # 마지막 숫자를 더해주고
        if msum > ssum:         # 저장되어있는 msum과 비교해가며 갱신
            msum = ssum
            return

    dfs(sr, sc + 1, ssum + board[sr][sc])       # 오른쪽으로 이동
    dfs(sr + 1, sc, ssum + board[sr][sc])       # 아래쪽으로 이동


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    msum = 9999999
    ssum = 0
    dfs(0, 0, ssum)
    
    print(f'#{tc} {msum}')

