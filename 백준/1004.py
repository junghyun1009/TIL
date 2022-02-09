# m = [-5, 1, 12, 1]

# a = [[0, 0, 2]]

t = int(input())
for tc in range(1,t+1):
    m = list(map(int, input().split()))
    n = int(input())
    a = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        a.append(tmp)

    cnt = 0

        # 둘 다 같은 원에 있는 경우
    for i in a:
        if pow((m[0]-i[0])**2+(m[1]-i[1])**2, 0.5) < i[2] and pow((m[2]-i[0])**2+(m[3]-i[1])**2,0.5) < i[2]:
            break

        elif pow((m[0]-i[0])**2+(m[1]-i[1])**2, 0.5) > i[2] and pow((m[2]-i[0])**2+(m[3]-i[1])**2,0.5) > i[2]:
            break


    for i in a:
        if pow((m[0]-i[0])**2+(m[1]-i[1])**2, 0.5) < i[2] and pow((m[2]-i[0])**2+(m[3]-i[1])**2, 0.5) > i[2]:
            cnt += 1

    for j in a:
        if pow((m[2]-j[0])**2+(m[3]-j[1])**2,0.5) < j[2] and pow((m[0]-j[0])**2+(m[1]-j[1])**2,0.5) > j[2]:
            cnt += 1

    print(cnt)

# cnt = 0

# for i in a:
#     if (i[0]-i[2] < m[0] < i[0]+i[2]) and (i[1]-i[2] < m[1] < i[1]+i[2]):
#         cnt += 1

# for j in a:
#     if (j[0]-j[2] < m[2] < j[0]+j[2]) and (j[1]-j[2] < m[3] < j[1]+j[2]):
#         cnt += 1