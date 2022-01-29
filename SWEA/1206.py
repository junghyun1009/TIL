for tc in range(1,11):
    t = int(input())
    tmp=list(map(int,input().split()))

    rlt = 0

    for i in range(2, len(tmp)-2):
        if (tmp[i]>tmp[i-2]) and (tmp[i]>tmp[i-1]) and (tmp[i]>tmp[i+1]) and (tmp[i]>tmp[i+2]):
            rlt = rlt + min(tmp[i]-tmp[i-2], tmp[i]-tmp[i-1], tmp[i]-tmp[i+1], tmp[i]-tmp[i+2])

    print(f'#{tc} {rlt}')

# n=8

# a=[0,0,3,5,2,4,9,0,6,4,0,6,0,0]

# main_tmp=[]
# for i in range(2,n+4):
#     tmp=0
    
#     if a[i]-a[i-2]>0 and a[i]-a[i-1]>0 and a[i]-a[i+1]>0 and a[i]-a[i+2]>0:
        
#         tmp=min(a[i]-a[i-2],a[i]-a[i-1],a[i]-a[i+1],a[i]-a[i+2])
#     main_tmp.append(tmp)
                              
# print(main_tmp)