import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    matrix = []

    for r in range(n):
        for c in range(n):
            if a[r][c] != 0 and visited[r][c] == 0:
                row = r
                col = c
                tmp_c = 0
                tmp_r = 0
                while a[row][col] != 0:
                    col += 1
                    tmp_c += 1
                    if col == n:
                        break
                col -= 1
                while a[row][col] != 0:
                    row += 1
                    tmp_r += 1
                    if row == n:
                        break
                row -= 1
                matrix.append([tmp_r * tmp_c, tmp_r, tmp_c])
                for i in range(r, row + 1):
                    for j in range(c, col + 1):
                        visited[i][j] = 1

    matrix = sorted(matrix)
    print(f'#{tc} {len(matrix)}', end=' ')
    for i in matrix:
        print(f'{i[1]} {i[2]}', end=' ')
    print()
