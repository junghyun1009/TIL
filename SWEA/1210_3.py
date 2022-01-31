for tc in range(1, 11):
    n = int(input())
    a = []
    for i in range(100):
        line = list(map(int, input().split()))
        a.append(line)

    # 2를 먼저 찾아
    b = a[-1]
    for number in range(len(b)):
        if b[number] == 2:
            now = [len(a)-1, number] # 현재 위치 정했어

    # 맨 윗줄에 도달할 때까지 반복
    while True:

        # 종료 조건
        if now[0] == -1 or now[0] == 0:
            print(f'#{tc} {now[1]}')
            break

        # 왼쪽으로 가
        if 0<=now[0]<len(a) and 0<=now[1]-1<len(a) and a[now[0]][now[1]-1] == 1:  
            while 0<=now[0]<len(a) and 0<=now[1]-1<len(a) and a[now[0]][now[1]-1] == 1:
                now[1] -= 1
            now[0] -= 1

        # 오른쪽으로 가
        elif 0<=now[0]<len(a) and 0<=now[1]+1<len(a) and a[now[0]][now[1]+1] == 1:
            while 0<=now[0]<len(a) and 0<=now[1]+1<len(a) and a[now[0]][now[1]+1] == 1:
                now[1] += 1
            now[0] -= 1

        # 위로 올라가
        else:
            # 맨 왼쪽으로 올라가는 경우
            if now[1] == 0:
                while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]+1] == 0:
                    now[0] -= 1
                    if now[0] == 0:
                        break
                now[0] -= 1
            # 맨 오른쪽으로 올라가는 경우
            elif now[1] == len(a)-1:
                while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]-1] == 0:
                    now[0] -= 1
                    if now[0] == 0:
                        break
                now[0] -= 1
            # 중간으로 올라가는 경우
            else:
                while a[now[0]-1][now[1]] == 1 and a[now[0]-1][now[1]-1] == 0 and a[now[0]-1][now[1]+1] == 0:
                    now[0] -= 1
                    if now[0] == 0:
                        break
                now[0] -= 1

    