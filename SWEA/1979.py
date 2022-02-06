t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))

# a = [[0,0,1,1,1],[1,1,1,1,0],[0,0,1,0,0],[0,1,1,1,1],[1,1,1,0,1]]
    count = 0
    b = []

    # 가로
    tmp_main = []
    tmp_a = []

    for row in a:
        tmp = []
        # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
        # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
        for i in range(len(row)-(m-1)):
            tmp.append(row[i:i+m])
        tmp_a.append(tmp)
    #print(tmp_a)

    for j in tmp_a:
        tmp_sum = []
        for k in j:
            tmp_sum.append(sum(k))
        tmp_main.append(tmp_sum)
    #print(tmp_main)


    for k in tmp_main:
        for i,j in enumerate(k):   

            if j==m :          
                if i==0 and k[i+1]!=m:
                    count=count+1             
                elif i==len(k)-1 and  k[i-1]!=m:
                    count=count+1
                elif i!=len(k)-1 and k[i-1]!=m and k[i+1]!=m :
                    count=count+1
                else:
                    pass

            else:
                pass

    #print(count)       


    # 세로
    for i in range(len(a[0])):
        b_ele = []
        for j in range(len(a)):
            b_ele.append(a[j][i])
        b.append(b_ele)
    #print(b)

    tmp_main2 = []
    tmp_b = []

    for row in b:
        tmp = []
        # 3개씩 자르면서 합이 3이면 좌우가 0이어야 돼
        # 3개씩 잘라서 3인거니까 나중에 글자수로 바꿔
        for i in range(len(row)-(m-1)):
            tmp.append(row[i:i+m])
        tmp_b.append(tmp)
    #print(tmp_a)

    for j in tmp_b:
        tmp_sum = []
        for k in j:
            tmp_sum.append(sum(k))
        tmp_main2.append(tmp_sum)
    #print(tmp_main2)


    for k in tmp_main2:
        for i,j in enumerate(k):   

            if j==m :          
                if i==0 and k[i+1]!=m:
                    count=count+1             
                elif i==len(k)-1 and  k[i-1]!=m:
                    count=count+1
                elif i!=len(k)-1 and k[i-1]!=m and k[i+1]!=m :
                    count=count+1
                else:
                    pass

            else:
                pass

    print(f'#{tc} {count}')

