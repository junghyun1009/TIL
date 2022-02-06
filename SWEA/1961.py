t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

    # a = [[1,2,3],[4,5,6],[7,8,9]]
    tmp = []
    tmp_a = []
    tmp_b = []

    for i in range(len(a[0])):
        empty = ''
        for j in range(len(a)-1,-1,-1):
            empty = empty + str(a[j][i])
        tmp.append(empty)
    #print(tmp)

    for i in range(len(a)-1,-1,-1):
        empty = ''
        for j in range(len(a[0])-1,-1,-1):
            empty = empty + str(a[i][j])
        tmp_a.append(empty)
    #print(tmp_a)

    for i in range(len(a[0])-1,-1,-1):
        empty = ''
        for j in range(len(a)):
            empty = empty + str(a[j][i])
        tmp_b.append(empty)
    #print(tmp_b)

    print(f'#{tc}')
    for i in range(len(tmp)):
        print(tmp[i], tmp_a[i], tmp_b[i])
