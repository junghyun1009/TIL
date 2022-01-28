for tc in range(1,11):
    t = int(input())
    tmp=[]
    n=list(map(int,input().split()))
    tmp=tmp+n

    rlt = 0

    for i in range(2, len(tmp)-2):
        if (tmp[i]>tmp[i-2]) and (tmp[i]>tmp[i-1]) and (tmp[i]>tmp[i+1]) and (tmp[i]>tmp[i+2]):
            rlt = rlt + min(tmp[i]-tmp[i-2], tmp[i]-tmp[i-1], tmp[i]-tmp[i+1], tmp[i]-tmp[i+2])

    print(f'#{tc} {rlt}')
