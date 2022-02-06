t = int(input())
for tc in range(1,t+1):
    n, f = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
# a = [
# [1,3,3,6,7],
# [8,13,9,12,8],
# [4,16,11,12,6],
# [2,4,1,23,2],
# [9,13,4,7,3]]
    rlt = []

    for m in range(len(a)-(f-1)):
        for k in range(len(a)-(f-1)):
            tmp = []
            for i in range(f):
                for j in range(f):
                    tmp.append(a[i+m][j+k])
            rlt.append(sum(tmp))
    print(f'#{tc} {max(rlt)}')
# for i in range(len(a)-2-1):
#     for j in range(len(a[0])-2):
#         tmp.append(sum(a[i][j:j+2]))
#         break
# rlt.append(sum(tmp))
# print(rlt)
# 일단은 2로 하는데 숫자 바꿔
#for i in range(len(a)-1):
# while True:
#     tmp = []

#     if i == 2:
#         break

#     for j in range(2):
#         tmp.append(sum(a[i][j:j+2]))
#         print(tmp)
#         i = i + 1
    
    #rlt.append(sum(tmp))
        #tmp.append(a[i][j]+a[i][j+1]+a[i+1][j]+a[i+1][j+1])
#print(rlt)
