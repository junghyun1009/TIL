#a = list(map(int, input().split('\n')))
a = [20, 7, 23, 19, 10, 15, 25, 8, 13]
a = sorted(a)
height_sum = sum(a)
liars = []

for ele in a:

    b = height_sum - 100 - ele

    if (ele != b) and (b in a):
        liars.append(ele)
    
    else:
        pass

real = set(a) - set(liars)
real_list = list(real)
print(sorted(real_list))