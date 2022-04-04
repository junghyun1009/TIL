import sys

sys.stdin = open('input.txt')


def BFS(si, sj, ei, ej):
    q = []      # 1. q, v 생성
    v = [[100000] * N for _ in range(N)]        # 매우 큰 값으로 초기화

    # 2. q 초기 데이터 삽입, v 표시
    q.append((si, sj))
    v[si][sj] = arr[si][sj]     # 시작점과 동일하게 초기화

    while q:
        ci, cj = q.pop(0)

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):       # 네 방향을 가보면서
            ni, nj = ci + di, cj + dj
            # 지금까지 저장된 복구시간에 다음 땅의 복구 시간을 더한게 더 작다면 갱신해주기
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = BFS(0, 0, N-1, N-1)
    
    print(f'#{tc} {ans}')

