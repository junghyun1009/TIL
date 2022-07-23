N, X = map(int, input().split())
num = list(map(int, input().split()))

for i in num:
    if i < X:
        print(i, end=' ')