n = int(input())
num = list(map(int, input().split()))

i = 0
rlt = 0
compare = 0


while True:
    cnt = 1
    if compare == n - 1:
        break

    for j in range(i, len(num)-1):

        if num[j] <= num[j+1]:
            cnt += 1

        else:
            if rlt < cnt:
                rlt = cnt
            i += 1
            compare += 1
            break
    else:
        if rlt < cnt:
            rlt = cnt
        compare += 1

i = 0
compare = 0

while True:
    cnt = 1
    if compare == n - 1:
        break

    for j in range(i, len(num) - 1):

        if num[j] >= num[j + 1]:
            cnt += 1

        else:
            if rlt < cnt:
                rlt = cnt
            i += 1
            compare += 1
            break
    else:
        if rlt < cnt:
            rlt = cnt
        compare += 1

print(rlt)