def dfs():
    if len(tmp) == cnt:
        rlt = x[:]
        cal_set.append(rlt)
        # print(cal_set)
        return cal_set

    for i in range(cnt):
        if i not in tmp:
            tmp.append(i)
            x.append(change[i])
            dfs()
            tmp.pop()
            x.pop()


n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))

# +:0, -:1, *:2, /:3
change = []
for i in range(4):
    for j in range(cal[i]):
        change.append(i)
# print(change)
cnt = len(change)
tmp = []
cal_set = []
x = []
dfs()
a = cal_set     # 연산자 인덱스 수열

max_cal = -10000000000
min_cal = 10000000000
# cals = []
for i in a:
    cal_rlt = num[0]
    for j in range(len(i)):
        if i[j] == 0:
            cal_rlt += num[j+1]
        elif i[j] == 1:
            cal_rlt -= num[j+1]
        elif i[j] == 2:
            cal_rlt *= num[j+1]
        else:
            if cal_rlt >= 0:
                cal_rlt //= num[j+1]
            else:
                cal_rlt = (-1) * cal_rlt
                cal_rlt = (-1) * (cal_rlt // num[j+1])

    if cal_rlt > max_cal:
        max_cal = cal_rlt

    if cal_rlt < min_cal:
        min_cal = cal_rlt

# print(cals)
# print(max(cals))
# print(min(cals))
print(max_cal)
print(min_cal)