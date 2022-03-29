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

    N = int(input())
    # 부모 인덱스에 자식 노드 저장
    left = [0] * (N+1)
    right = [0] * (N+1)
    order = [0]

    for i in range(2, N+1):
        if i % 2 == 0:
            left[i//2] = i
        else:
            right[i//2] = i

    order = inorder(1)
    # print(order)
    for i in range(N+1):
        if order[i] == 1:
            a = i
        elif order[i] == N//2:
            b = i
    print(f'#{tc} {a} {b}')

