num = list(map(int, input().split()))

tmp_sum = 0

for i in num:
    tmp_sum += i ** 2

print(tmp_sum % 10)