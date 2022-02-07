t = int(input())
for tc in range(1,t+1):
    n = int(input())
    a = []
    for i in range(n):
        row = list(map(int, ' '.join(input()).split()))
        a.append(row)

    sum = 0
    middle = int((len(a)-1)/2)

    # 가운데
    for idx in range(len(a)):
        sum = sum + a[idx][middle]

    # 가운데에서 왼쪽
    for i in range(middle-1,-1,-1):
        tmp = 0
        for j in range(middle-i,len(a)-middle+i):
            tmp = tmp + a[j][i]
        sum = sum + tmp

    # 가운데에서 오른쪽
    for i in range(middle+1,len(a)):
        tmp = 0
        for j in range(i-middle,len(a)-i+middle):
            tmp = tmp + a[j][i]
        sum = sum + tmp

    print(f'#{tc} {sum}')