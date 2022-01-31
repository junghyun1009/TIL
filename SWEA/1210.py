a = [[1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0 ,0, 2]]

b = a[0]

for number in range(len(b)):
    if number == 0 and b[number] == 1:
        now = [0, 0]
        for line in range(1, len(a)):
            if a[line][0] == 1 and a[line][1] == 0:
                now[0] += 1
            elif a[line][0] == 1 and a[line][1] == 1:
                now[0] += 1
                now[1] += 1
                number = now[1]
                break
    
    elif number != 0 and number != len(b)-1:
        while now[0] != 9:
            # 오른쪽으로 이동
            if a[now[0]][now[1]+1] == 1:
                now[1] += 1
                if a[now[0]][now[1]+1] == 0:
                    now[0] +=1
            
            #왼쪽으로 이동
            elif a[now[0]][now[1]-1] == 1:
                now[1] -= 1
                
            # 아래로 이동
            elif a[now[0]+1][now[1]] == 1:
                now[0] += 1

                # 왼쪽으로 이동
                if a[now[0]][now[1]-1] == 1:
                    now[1] -= 1
                    print(now)


