import sys
input = sys.stdin.readline

tmp = [list(input()) for _ in range(4)]
K = int(input())
move = [list(map(int, input().split(' '))) for _ in range(K)]

wheel = []
for r in tmp:
    wheel.append(r[0:8])

# print(wheel)
# print(move)

for m in move:
    check_a = [wheel[0][2], wheel[1][6]]
    check_b = [wheel[1][2], wheel[2][6]]
    check_c = [wheel[2][2], wheel[3][6]]

    turn = [0, 0, 0]

    if check_a[0] != check_a[1]:
        turn[0] = 1
    if check_b[0] != check_b[1]:
        turn[1] = 1
    if check_c[0] != check_c[1]:
        turn[2] = 1

    # print(turn)

    # 돌아가는 톱니바퀴
    if m[1] == -1:
        out = wheel[m[0]-1].pop(0)
        wheel[m[0]-1].append(out)

    else:
        out = wheel[m[0]-1].pop()
        wheel[m[0]-1].insert(0, out)

    # print('!', wheel)

    org = m[1]

    # 오른쪽 톱니바퀴
    for r in range(m[0]-1, 3):
        # 다른 극이면
        if turn[r] == 1:
            direction = (-1) * org

            if direction == -1:
                out = wheel[r+1].pop(0)
                wheel[r+1].append(out)

            else:
                out = wheel[r+1].pop()
                wheel[r+1].insert(0, out)

            org = direction

        # 같은 극이면
        else:
            break

    # print('!!', wheel)
    
    org = m[1]

    # 왼쪽 톱니바퀴
    for r in range(m[0]-2, -1, -1):
        # 다른 극이면
        if turn[r] == 1:
            direction = (-1) * org

            if direction == -1:
                out = wheel[r].pop(0)
                wheel[r].append(out)

            else:
                out = wheel[r].pop()
                wheel[r].insert(0, out)

            org = direction

        # 같은 극이면
        else:
            break
            
    # print('!!!', wheel)
    # print(wheel)

cnt = 0
if wheel[0][0] == '1':
    cnt += 1
if wheel[1][0] == '1':
    cnt += 2
if wheel[2][0] == '1':
    cnt += 4
if wheel[3][0] == '1':
    cnt += 8

print(cnt)