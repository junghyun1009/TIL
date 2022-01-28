for tc in range(1,11):
    t = int(input())
    tmp=[]
    for i in range(1,101):
        n=list(map(int,input().split()))
        tmp=tmp+[n]

        sum_list = []
        empty = []
        dia_1 = []
        dia_2 = []
        j = 0

    for i in tmp:
        sum_list.append(sum(i))

    while j < len(tmp):
        list_row = []
        for k in range(len(tmp)):
            list_row.append(tmp[k][j])
        empty.append(list_row)
        j = j + 1

    for k in empty:
        sum_list.append(sum(k))

    for l in range(len(tmp)):
        dia_1.append(tmp[l][l])
        dia_2.append(tmp[l][len(tmp)-1-l])

    sum_list.append(sum(dia_1))
    sum_list.append(sum(dia_2))

    print(f'#{t} {max(sum_list)}')