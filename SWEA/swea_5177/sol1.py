import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())        # 노드 수
    a = [0] + list(map(int, input().split()))       # 트리에 순서대로 넣을 값이 저장된 리스트

    tree = [0] * (n + 1)        # 각 노드에 저장된 값을 확인할 트리
    tree[1] = a[1]      # 가장 root인 값 저장
    for i in range(2, n + 1):
        tree[i] = a[i]      # 해당 노드에 해당 번째 값 저장
        j = i       # 계속 값의 크기를 비교해야하므로 인덱스 기억해두기
        while a[j] < tree[i//2]:        # 부모가 더 작아질 때까지 반복
            tree[i], tree[i//2] = tree[i//2], tree[i]       # 부모가 더 크다면 부모와 자리 바꾸기
            i = i // 2      # 다음 부모 인덱스

    rlt = 0

    while True:
        if n == 1:
            break

        n = n // 2      # 부모 노드로 올라가며 저장된 값 더해주기
        rlt += tree[n]

    print(f'#{tc} {rlt}')

