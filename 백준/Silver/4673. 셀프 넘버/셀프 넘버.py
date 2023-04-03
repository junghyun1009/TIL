def eachsum(n):
    # 자릿수 파악
    each = 0
    m = n
    ans = 0
    while True:
        if 1 <= m < 10:
            each += m
            ans = n + each
            return ans
        q = m // 10
        r = m % 10
        each += r
        m = q

def selfnum(arr, n):
    a = n
    while n <= 10000:
        a = eachsum(n)
        arr[a] = a
        n = a
    return arr

arr = [0] * 20000    
one = selfnum(arr, 1)

for i in range(3, 10001):
   tmp = selfnum(one, i)
   one = tmp

for j in range(1, 10001):
    if tmp[j] == 0:
        print(j)