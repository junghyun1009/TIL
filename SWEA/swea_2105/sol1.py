import sys

sys.stdin = open('input.txt')

def dfs(r, c):
    stack = []
    dessert = []
    stack.append([r, c])
    dessert.append(a[r][c])

    while True:
        x, y = stack[-1]
        # 오아 왼아 왼위 오위
        dx = [1, 1, -1, -1]
        dy = [1, -1, -1, 1]

        i = 0
        cnt_a = 0   # 오아=왼위
        cnt_b = 0   # 왼아=오위
        cnt_c = 0
        cnt_d = 0

        while True:
            if i == 4:
                return stack
            nx = x + dx[i]
            ny = y + dy[i]

            if i == 0:
                if 1 <= nx < n-1 and 2 <= ny < n and a[nx][ny] not in dessert:
                    stack.append([nx, ny])
                    dessert.append(a[nx][ny])
                    x, y = stack[-1]
                    cnt_a += 1
                    print(1, cnt_a)

                else:
                    i += 1

            elif i == 1:
                if 2 <= nx < n and 1 <= ny < n-1 and a[nx][ny] not in dessert:
                    stack.append([nx, ny])
                    dessert.append(a[nx][ny])
                    x, y = stack[-1]
                    cnt_b += 1
                    print(2, cnt_b)

                else:
                    i += 1

            elif i == 2:
                while True:
                    if cnt_c == cnt_a:
                        print(3, cnt_c)
                        break

                    if 1 <= nx < n-1 and 0 <= ny < n-2 and a[nx][ny] not in dessert:
                        stack.append([nx, ny])
                        dessert.append(a[nx][ny])
                        x, y = stack[-1]
                        cnt_c += 1
                        print(3, cnt_c)

                    else:
                        i += 1

            else:
                while True:
                    if cnt_d == cnt_b:
                        break

                    if 0 <= nx < n-2 and 1 <= ny < n-1 and a[nx][ny] not in dessert:
                        stack.append([nx, ny])
                        dessert.append(a[nx][ny])
                        x, y = stack[-1]
                        cnt_d += 1
                        print(4, cnt_d)

                    elif [nx, ny] == stack[0]:
                        cnt_d += 1

                    else:
                        i += 1


T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    print(dfs(0, 1))
    
    print(f'#{tc} ')

