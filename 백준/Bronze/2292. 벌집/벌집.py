N = int(input())

n = 1
while True:
    if N <= (3 * n * n - 3 * n + 1):
        print(n)
        break
    else:
        n += 1