n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]

# print(n)
# print(a)
# print(m)
# print(b)

for i in b:
    if i[0] == 1:       # 남자라면

        cnt = n // i[1]
        for j in range(1, cnt+1):
            a[i[1]*j-1] = int(not a[i[1]*j-1])


    else:
        if n - i[1] > i[1] - 1:     # 왼쪽에 더 조금 남았으면
            for j in range(i[1]):
                if a[i[1]-1-j] == a[i[1]-1+j]:
                    start = i[1]-1-j
                    end = i[1]-1+j

            for k in range(start, end+1):
                a[k] = int(not a[k])

        else:       # 오른쪽에 더 조금 남았으면
            for j in range(n-i[1]+1):
                if a[i[1]-1-j] == a[i[1]-1+j]:
                    start = i[1]-1-j
                    end = i[1]-1+j

            for k in range(start, end+1):
                a[k] = int(not a[k])

cnt = 0
for i in a:
    cnt += 1
    if (cnt == 1) or (cnt % 20 != 1):
        print(i, end=' ')
    else:
        print()
        print(i, end=' ')

