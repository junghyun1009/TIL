t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
# n = 5
# a = [2, 5, 3]
    rlt = []

    for i in range(1,n+1):
        if i in a:
            continue
        else:
            rlt.append(i)

    rlt.sort()

    print(f'#{tc}', end=' ')

    for i in rlt:
        print(i, end=' ')
        
    print()