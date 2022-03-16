import sys

sys.stdin = open('input.txt')

def preorder(v):
    global cnt
    if v:
        # print(v)
        cnt += 1
        preorder(left[v])
        preorder(right[v])
    return cnt

T = int(input())

for tc in range(1, T + 1):

    e, n = map(int, input().split())
    a = list(map(int, input().split()))

    b = []
    cnt = 0

    for i in range(e):
        b.append([a[2*i], a[2*i+1]])

    # print(b)

    left = [0] * (e+2)
    right = [0] * (e+2)

    for i in b:
        if left[i[0]] == 0:
            left[i[0]] = i[1]
        else:
            right[i[0]] = i[1]

    # print(left)
    # print(right)

    print(f'#{tc} {preorder(n)}')

