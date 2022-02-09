a = [2, 4, 7, 10]
tmp = []
tmp_main = []
rlt = []

for i in range(len(a)):
    for j in range(i+1,len(a)):
        tmp.append(a[i]*a[j])

tmp = sorted(tmp)
# print(tmp)

for a in tmp:
    b = str(a) #'14'
    len_b = len(b)
    if len_b == 1:
        tmp_main.append([a])

    elif len_b > 1:
        tmp_b = []
        for num in range(len_b-1,0,-1):
            tmp_b.append(a//10**num)
        tmp_b.append(a%10)
        tmp_main.append(tmp_b)

# print(tmp_main)
# tmp_main = sorted(tmp_main)

for i in tmp_main:
    if len(i) == 1:
        rlt.append(i)

    for idx in range(len(i)-1):
        if i[idx] > i[idx+1]:
            continue
        else:
            rlt.append(i)

# print(rlt)

if len(rlt) == 0:
    print('-1')
    print()

maximum = rlt[-1]
#print(f'# {tc}', end='')
for i in maximum:
    print(i, end='')
print()

