import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
K = int(input())
apple = [list(map(int, input().split(' '))) for _ in range(K)]
L = int(input())
move = [list(input().split(' ')) for _ in range(L)]
move.append(['100000', ''])

# print(apple)
# print(move)

board = [[0] * N for _ in range(N)]
for a in apple:
    board[a[0]-1][a[1]-1] = 1
# print(board)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

snake = deque()
snake.append([0, 0])
d = 0
time = 0
flag = 0

for m in move:

    # print(m, d)
    for t in range(time, int(m[0])):
        # print(time, snake)
        target = [snake[-1][0] + dr[d], snake[-1][1] + dc[d]]
        # print(target)
        # 다음 칸에 사과가 있는 경우
        if (0 <= target[0] < N) and (0 <= target[1] < N) and board[target[0]][target[1]] == 1:
            time += 1
            snake.append([target[0], target[1]])
            board[target[0]][target[1]] = 0
            # print('!')
        # 다음 칸이 벽인 경우
        elif target[0] < 0 or target[0] >= N or target[1] < 0 or target[1] >= N:
            time += 1
            flag = 1
            # print('!!')
            break
        # 다음 칸이 뱀인 경우
        elif target in snake:
            time += 1
            flag = 1
            # print('!!!')
            break
        # 다음 칸이 빈칸인 경우
        else:
            time += 1
            snake.append(target)
            snake.popleft()
            # print('!!!!')

    if flag == 1:
        break

    if m[1][0] == 'D':
        if d != 3:
            d += 1
        else:
            d = 0

    else:
        if d != 0:
            d -= 1
        else:
            d = 3
    
print(time)
