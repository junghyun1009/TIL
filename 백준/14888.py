def dfs():
    if len(tmp) == cnt:
        rlt = tmp[:]
        cal_set.append(rlt)
        # print(cal_set)
        return cal_set

    for i in range(cnt):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()


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
dfs()
a = cal_set     # 연산자 인덱스 수열
# print(a)

b = []
for i in a:
    tmp_a = []
    for j in i:
        tmp_a.append(change[j])
    b.append(tmp_a)
# print(b)

cals = []
for i in b:
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

    cals.append(cal_rlt)

# print(cals)
print(max(cals))
print(min(cals))