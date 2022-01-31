a = [[1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 1, 1, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
[1, 0, 0, 0, 1, 0, 1, 0, 0, 1], [1, 1, 1, 1, 1, 0, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
[1, 0, 0, 0, 1, 0, 1, 0 ,0, 2]]

b = a[-1]
for number in range(len(b)):
    if b[number] == 2:
        now = [len(a)-1, number]

# 2가 왼쪽에 붙어있는 경우
if now[1] == 0:
    while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]+1] == 0:
        now[0] -= 1
    now[0] -= 1

# 2가 오른쪽에 붙어있는 경우
elif now[1] == len(a)-1:
    while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]-1] == 0:
        now[0] -= 1
    now[0] -= 1


# 2가 가운데에 있는 경우
else:
    while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]-1] == 0 and a[now[0]-1][now[1]+1] == 0:
        now[0] -= 1
    now[0] -= 1


while True:

    if now[0] == 0:
        print(now[1]) # 종료
        break

    # 왼쪽으로 가는 경우
    if a[now[0]][now[1]-1] == 1:  
        while a[now[0]][now[1]-1] == 1:
            now[1] -= 1

    # 위로 가는 경우
    elif a[now[0]-1][now[1]] == 1: 
        while a[now[0]-1][now[1]] == 1:
            now[0] -= 1
            if a[now[0]-1][now[1]-1] == 1 or a[now[0]+1][now[1]+1] ==1:
                break
        now[0] -= 1



