import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split(' '))
num = [list(map(int, input().split(' '))) for _ in range(N)]
move = list(map(int, input().split(' ')))

# print(num)
# print(move)

cur = [x, y]
front = 5
bottom = 6
dice = [0, 0, 0, 0, 0, 0, 0]

for m in move:
    if m == 1:
        # 동쪽, 앞뒤 안 바뀜
        if front == 1:
            route = [5, 3, 2, 4]
        elif front == 2:
            route = [4, 1, 3, 6]
        elif front == 3:
            route = [6, 2, 1, 5]
        elif front == 4:
            route = [5, 1, 2, 6]
        elif front == 5:
            route = [6, 3, 1, 4]
        else:
            route = [4, 2, 3, 5]

        if 0 <= cur[1]+1 < M:
            cur[1] += 1
            # print(cur)
            for r in range(4):
                if route[r] == bottom and r != 3:
                    bottom = route[r+1]
                    break
                elif route[3] == bottom:
                    bottom = route[0]
                    break
                    
            if num[cur[0]][cur[1]] == 0:
                num[cur[0]][cur[1]] = dice[bottom]
            else:
                dice[bottom] = num[cur[0]][cur[1]]
                num[cur[0]][cur[1]] = 0
            # print(dice)
            print(dice[7-bottom])
        else:
            pass  

    elif m == 2:
        # 서쪽, 앞뒤 안 바뀜
        if front == 1:
            route = [4, 2, 3, 5]
        elif front == 2:
            route = [6, 3, 1, 4]
        elif front == 3:
            route = [5, 1, 2, 6]
        elif front == 4:
            route = [6, 2, 1, 5]
        elif front == 5:
            route = [4, 1, 3, 6]
        else:
            route = [5, 3, 2, 4]

        if 0 <= cur[1]-1 < M:
            cur[1] -= 1
            # print(cur)
            for r in range(4):
                if route[r] == bottom and r != 3:
                    bottom = route[r+1]
                    break
                elif route[3] == bottom:
                    bottom = route[0]
                    break
                    
            if num[cur[0]][cur[1]] == 0:
                num[cur[0]][cur[1]] = dice[bottom]
            else:
                dice[bottom] = num[cur[0]][cur[1]]
                num[cur[0]][cur[1]] = 0
            # print(dice)
            print(dice[7-bottom])
        else:
            pass  

    elif m == 3:
        # 북쪽, 좌우 안 바뀜
        route = [bottom, 7-front, 7-bottom, front]
        if 0 <= cur[0]-1 < N:
            cur[0] -= 1
            # print(cur)
            front, bottom = bottom, 7 - front
            
            if num[cur[0]][cur[1]] == 0:
                num[cur[0]][cur[1]] = dice[bottom]
            else:
                dice[bottom] = num[cur[0]][cur[1]]
                num[cur[0]][cur[1]] = 0
            # print(dice)
            print(dice[7-bottom])
        else:
            pass        

    else:
        # 남쪽, 좌우 안 바뀜
        route = [front, 7-bottom, 7-front, bottom]
        if 0 <= cur[0]+1 < N:
            cur[0] += 1
            # print(cur)
            front, bottom = 7 - bottom, front
            
            if num[cur[0]][cur[1]] == 0:
                num[cur[0]][cur[1]] = dice[bottom]
            else:
                dice[bottom] = num[cur[0]][cur[1]]
                num[cur[0]][cur[1]] = 0
            # print(dice)
            print(dice[7-bottom])
        else:
            pass
    
