import sys

sys.stdin = open('input.txt')

def inorder(v):     # 중위 순회 함수(들어가는건 인덱스)
    if v:
        inorder(left[v])
        print(a[v][1], end='')      # 출력하는건 인덱스에 해당하는 알파벳이어야 함
        inorder(right[v])

for tc in range(1, 11):

    n = int(input())
    a = [[0]]       # 트리에 대한 정보를 받아올 list(인덱스 안 헷갈리게 0번째 인덱스는 미리 채움)
    left = [0] * (n+1)      # 부모인덱스에 왼쪽 자식 저장
    right = [0] * (n+1)     # 부모인덱스에 오른쪽 자식 저장

    for i in range(n):
        node, value, *leaf = input().split()
        a.append([int(node), value, leaf])

    for i in range(1, n + 1):
        if len(a[i][2]) == 2:       # 자식이 두명인 경우 왼쪽 자식과 오른쪽 자식에 각각 저장
            left[i] = int(a[i][2][0])
            right[i] = int(a[i][2][1])

        elif len(a[i][2]) == 1:     # 자식이 한명인 경우 왼쪽 자식에 저장
            left[i] = int(a[i][2][0])

    # print(a)
    # print(f'left={left}')
    # print(f'right={right}')

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
