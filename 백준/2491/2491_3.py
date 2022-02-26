n = int(input())
a = list(map(int, input().split()))

i = 0
cnt = 1
rlt = 1
while True:

    if i == len(a) - 1:
        if rlt < cnt:
            rlt = cnt
        break

    if a[i] <= a[i+1]:
        cnt += 1
        i += 1

    else:
        if rlt < cnt:
            rlt = cnt
        cnt = 1
        i += 1

i = 0
cnt = 1
while True:

    if i == len(a) - 1:
        if rlt < cnt:
            rlt = cnt
        break

    if a[i] >= a[i+1]:
        cnt += 1
        i += 1

    else:
        if rlt < cnt:
            rlt = cnt
        cnt = 1
        i += 1

print(rlt)