import sys

sys.stdin = open('input.txt')


def dfs(a):     # 해당 배열에서 가질 수 있는 사각형의 [가로, 세로] 경우의 수를 모두 구하는 함수
    if len(a) == 2:
        rlt.append(a)
        return

    for i in range(1, N-1):
        dfs(a + [i])


def bfs(x, y):      # 디저트카페 순회하는 함수
    global maxcnt, rlt

    # 오아 왼아 왼위 오위
    dr = [1, 1, -1, -1]
    dc = [1, -1, -1, 1]

    for each in rlt:        # 각각의 사각형([가로, 세로])에 대해서
        # print('----')
        # print(each)
        dessert = [0] * 101     # 디저트 카페 방문 표시(인덱스와 맞춰주기)
        w = each[0]     # 사각형의 가로 길이
        h = each[1]     # 사각형의 세로 길이
        sr = x      # 순회를 시작하는 행
        sc = y      # 순회를 시작하는 열
        flag = 1        # 정상 종료를 판단하기 위한 변수

        for dir in range(4):        # 네 방향을 순회하며
            if flag == 0:       # 비정상 종료
                break

            if dir % 2 == 0:        # 가로
                for _ in range(w):
                    nr = sr + dr[dir]       # 다음 칸으로 한칸씩 이동
                    nc = sc + dc[dir]
                    # print(1, [nr, nc])

                    # 이동하려는 인덱스가 범위 내에 있고, 아직 방문 안한 카페라면
                    if 0 <= nr < N and 0 <= nc < N and dessert[cafe[nr][nc]] == 0:
                        dessert[cafe[nr][nc]] = 1       # 방문 표시
                        sr = nr     # 현재 위치 갱신
                        sc = nc

                    else:       # 아니라면 중단
                        flag = 0
                        break

            else:       # 세로
                for _ in range(h):
                    nr = sr + dr[dir]
                    nc = sc + dc[dir]
                    # print(2, [nr, nc])

                    if 0 <= nr < N and 0 <= nc < N and dessert[cafe[nr][nc]] == 0:
                        dessert[cafe[nr][nc]] = 1
                        sr = nr
                        sc = nc

                    else:
                        flag = 0
                        break

        # print(flag)
        if flag == 1:       # 정상 종료된 경우
            length = 2 * (w + h)        # 둘레 계산
            # print(length)
            if maxcnt < length:
                maxcnt = length         # 최대 둘레 갱신

    return maxcnt


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    maxcnt = -1

    rlt = []
    visited = [0] * (N - 1)
    dfs([])
    # print(rlt)

    most = -1
    for r in range(N-2):
        for c in range(1, N-1):
            a = bfs(r, c)
            # print([r, c], a)
            if most < a:
                most = a

    print(f'#{tc} {most}')

