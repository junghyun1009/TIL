n = int(input())
a = list(map(int, input().split()))
m = int(int(input()))
b = list(map(int, input().split()))

a = sorted(a)

def binary(a, start, end, t):

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == t:
            return 1

        elif a[mid] > t:
            end = mid - 1

        else:
            start = mid + 1

    return 0

for i in b:
    print(binary(a, 0, n-1, i))