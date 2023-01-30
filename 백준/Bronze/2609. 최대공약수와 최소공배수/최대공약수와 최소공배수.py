A, B = map(int, input().split())

# 최대공약수
# 1. 일단 작은 수를 찾아
small = min(A, B)
big = max(A, B)
# 2. 숫자 감소시키면서 둘다 나눠보기
for i in range(small, 0, -1):
    if (small % i == 0) and (big % i == 0):
        ans = i
        q1 = int(small/i)
        q2 = int(big/i)
        break
print(ans)
print(ans * q1 * q2)