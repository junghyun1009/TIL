import sys
from pprint import pprint

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    board = [[0] * N for _ in range(N)]

    mid = N // 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    board[mid-1][mid-1] = 2
    board[mid][mid] = 2

    # pprint(board)

    for a in A:
        board[a[1]-1][a[0]-1] = a[2]
        # pprint(board)

        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        r = a[1] - 1
        c = a[0] - 1

        for i in range(8):

            stack = []

            for p in range(1, N):
                nr = r + dr[i] * p
                nc = c + dc[i] * p

                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == 2//a[2]:
                    stack.append([nr, nc])
                    # print(p)
                    # print(stack)

                elif 0 <= nr < N and 0 <= nc < N and board[nr][nc] == a[2]:
                    # print(p)
                    for j in stack:
                        board[j[0]][j[1]] = a[2]

                    break

                else:
                    break

    # pprint(board)
    cnt1 = 0
    cnt2 = 0

    for i in board:
        for j in i:
            if j == 1:
                cnt1 += 1

            elif j == 2:
                cnt2 += 1

    print(f'#{tc} {cnt1} {cnt2}')