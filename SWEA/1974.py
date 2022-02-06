t = int(input())
for tc in range(1,t+1):
    a = []
    for n in range(9):
        line = list(map(int, input().split()))
        a.append(line)
# a = [
# [7, 3, 6, 4, 2, 9, 5, 8, 1], 
# [5, 8, 9, 1, 6, 7, 3, 2, 4], 
# [2, 1, 4, 5, 8, 3, 6, 9, 7], 
# [8, 4, 7, 9, 3, 6, 1, 5, 2], 
# [1, 5, 3, 8, 4, 2, 9, 7, 6], 
# [9, 6, 2, 7, 5, 1, 8, 4, 3], 
# [4, 2, 1, 3, 9, 8, 7, 6, 5], 
# [3, 9, 5, 6, 7, 4, 2, 1, 8], 
# [6, 7, 8, 2, 1, 5, 4, 3, 9]
# ]

    b = []
    c = []
    flag = 1

    # 가로
    for i in a:
        for num in range(1,10):
            if (num in i) and (i.count(num) == 1):
                continue
            else:
                flag = 0

    # 세로
    for i in range(len(a[0])):
        tmp = []
        for j in range(len(a)):
            tmp.append(a[j][i])
        b.append(tmp)

    for i in b:
        for num in range(1,10):
            if (num in i) and (i.count(num) == 1):
                continue
            else:
                flag = 0

    # 네모
    for i in range(0,9,3):
        for j in range(0,9,3):
            tmp_a = []
            for k in range(3):
                for m in range(3):
                    tmp_a.append(a[k+i][m+j])
            c.append(tmp_a)

    for i in c:
        for num in range(1,10):
            if (num in i) and (i.count(num) == 1):
                continue
            else:
                flag = 0

    print(f'#{tc} {flag}')
