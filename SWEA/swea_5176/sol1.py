import sys

sys.stdin = open('input.txt')

def inorder(v):
    if v:
        inorder(left[v])
        order.append(v)
        inorder(right[v])
    return order

T = int(input())

for tc in range(1, T + 1):

    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n+1)
    order = [0]

    for i in range(2, n + 1):
        if i % 2 == 0:
            left[i//2] = i
        else:
            right[i//2] = i

    # print(left)
    # print(right)
    order = inorder(1)
    # print(order)
    for j in range(n+1):
        if order[j] == 1:
            a = j
        elif order[j] == n//2:
            b = j

    print(f'#{tc} {a} {b}')

