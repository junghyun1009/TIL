t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

# a = [[0,0,1,1,1],[1,1,1,1,0],[0,0,1,0,0],[0,1,1,1,1],[1,1,1,0,1]]
    count = 0
    b = []

    # 가로
    for row in a:
        tmp = []
        # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
        # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
        for i in range(len(row)-(k-1)):
            tmp.append(row[i:i+k])
        #print(tmp)

        tmp_sum = []
        for j in tmp:
            tmp_sum.append(sum(j))
        #print(tmp_sum)

        if tmp_sum.count(k) == 1:
            count += 1

    # 세로
    for i in range(len(a[0])):
        b_ele = []
        for j in range(len(a)):
            b_ele.append(a[j][i])
        b.append(b_ele)
    #print(b)

    for row in b:
        tmp = []
        # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
        # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
        for i in range(len(row)-(k-1)):
            tmp.append(row[i:i+k])
        #print(tmp)

        tmp_sum = []
        for j in tmp:
            tmp_sum.append(sum(j))
        #print(tmp_sum)

        if tmp_sum.count(k) == 1:
            count += 1

    print(f'#{tc} {count}')

