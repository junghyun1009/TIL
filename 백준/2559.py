# a = [3,-2,-4,-9,0,3,7,13,8,-3]
# k = 5
n, k = map(int, input().split())
a = list(map(int, input().split()))
tmp_sum = sum(a[0:k])
tmp_max = sum(a[0:k])

for idx in range(k,len(a)):
    tmp = tmp_sum + a[idx] - a[idx-k]
    tmp_sum = tmp
    if tmp_max <= tmp:
        tmp_max = tmp
print(tmp_max)

# tmp_sum = 0

# for idx in range(len(a)-(k-1)):
#     tmp = 0
#     for num in range(k):
#         tmp = tmp + a[idx+num]
#     if tmp_sum > tmp:
#         continue
#     else:
#         tmp_sum = tmp

# print(tmp_sum)