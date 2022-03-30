import sys

sys.stdin = open('input.txt')


def merge(a):
    global cnt

    if len(a) == 1:
        return a

    middle = len(a) // 2
    left = merge(a[0:middle])
    right = merge(a[middle:len(a)])

    rlt = []
    x, y = 0, 0

    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            rlt.append(left[x])
            x += 1
        else:
            rlt.append(right[y])
            y += 1

    if left[-1] > right[-1]:
        cnt += 1

    rlt += left[x:]
    rlt += right[y:]

    return rlt


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    ans = merge(A)

    print(f'#{tc} {ans[N//2]} {cnt}')

