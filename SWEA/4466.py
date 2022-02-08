# a = [100,90,80,98,70,88,65,98,99]
# k = 2
t = int(input())
for tc in range(1,t+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    max_sum = 0

    a = sorted(a)
    a = a[::-1]

    for i in range(k):
        max_sum += a[i]

    print(f'#{tc} {max_sum}')