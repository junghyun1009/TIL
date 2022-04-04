import sys

sys.stdin = open('input.txt')


def DFS(n, cnt, ssum, lst):
    global sol

    if cnt > C:     # 가지치기
        return

    if n == M:
        if cnt <= C and sol < ssum:
            sol = ssum
        return

    DFS(n+1, cnt + lst[n], ssum + lst[n]**2, lst)       # 포함시키는 경우(가지칠 때는 얘 먼저 하는게 훨씬 빠름)
    DFS(n+1, cnt, ssum, lst)        # 포함시키지 않는 경우


T = int(input())

for tc in range(1, T + 1):

    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    
    # 메모이제이션 활용
    mem = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            sol = 0
            DFS(0, 0, 0, arr[i][j:j+M])
            mem[i][j] = sol
    
    for i1 in range(N):     # 일꾼1
        for j1 in range(N-M+1):
            sol = 0
            DFS(0, 0, 0, arr[i1][j1:j1+M])
            t1 = sol

            for i2 in range(i1, N):     # 일꾼2
                sj = 0
                if i1 == i2:        # 같은 열에 있는 경우
                    sj = j1 + M
                for j2 in range(sj, N-M+1):
                    ans = max(ans, mem[i1][j1] + mem[i2][j2])

    print(f'#{tc} {ans}')