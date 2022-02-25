n = int(input())
num = list(map(int, input().split()))

i = 0
increase = []
decrease = []

while True:
    cnt = 1
    if len(increase) == n - 1:
        break

    for j in range(i, len(num)-1):

        if num[j] <= num[j+1]:
            cnt += 1

        else:
            increase.append(cnt)
            i += 1
            break
    else:
        increase.append(cnt)

a = max(increase)

i = 0
while True:
    cnt = 1
    if len(decrease) == n - 1:
        break

    for j in range(i, len(num)-1):

        if num[j] >= num[j+1]:
            cnt += 1

        else:
            decrease.append(cnt)
            i += 1
            break

    else:
        decrease.append(cnt)

b = max(decrease)

if a > b:
    print(a)
else:
    print(b)