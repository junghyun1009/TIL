import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    matrix = []
    row = 0
    col = 0
    tmp = 0

    r = 0
    c = 0
    for r in range(tmp, n):
        if tmp == row:
            col = 0

        for c in range(col, n):

            if a[r][c] != 0:
                while a[row][col] != 0:
                    col += 1
                    tmp_c = col
                    if col == n:
                        break
                col -= 1
                while a[row][col] != 0:
                    row += 1
                    tmp_r = row
                    if row == n:
                        break
                matrix.append([tmp_r, tmp_c])
                break


    print(matrix)
    print(f'#{tc} ')

