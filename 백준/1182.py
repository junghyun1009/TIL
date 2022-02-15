n, s = map(int,input().split())
a = list(map(int, input().split()))
cnt = 0

tmp_main = []
for i in range(1<<n):
    tmp = []
    for j in range(n):
        if i & (1<<j):
            tmp.append(a[j])
    tmp_main.append(tmp)

for i in tmp_main:
    if sum(i) == s:
        cnt += 1

if s == 0 and cnt >= 1:
    cnt = cnt - 1
    print(cnt)

else:
    print(cnt)