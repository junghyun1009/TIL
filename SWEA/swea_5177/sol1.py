import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    a = [0] + list(map(int, input().split()))

    tree = [0] * (n + 1)
    tree[1] = a[1]
    for i in range(2, n + 1):
        tree[i] = a[i]
        j = i
        while a[j] < tree[i//2]:
            tree[i], tree[i//2] = tree[i//2], tree[i]
            i = i // 2

    # print(a)
    # print(tree)
    rlt = 0

    while True:
        if n == 1:
            break

        n = n // 2
        rlt += tree[n]

    print(f'#{tc} {rlt}')

