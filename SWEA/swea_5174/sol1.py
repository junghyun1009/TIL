import sys

sys.stdin = open('input.txt')


def preorder(v):
    '''
    전위 순회를 하며 subtree의 노드를 세는 함수
    :param v: 시작 노드
    :return: cnt (subtree에 속한 노드 수)
    '''
    global cnt
    if v:
        cnt += 1        # print를 하는 대신 cnt를 증가시켜주면 노드의 수를 셀 수 있음
        preorder(left[v])
        preorder(right[v])
    return cnt


T = int(input())

for tc in range(1, T + 1):

    e, n = map(int, input().split())        # e : 간선 수, n : 루트 노드 지정
    a = list(map(int, input().split()))     # 간선 정보 받을 리스트

    b = []
    cnt = 0

    for i in range(e):      # 간선 정보를 분리해서 저장하기 위함
        b.append([a[2*i], a[2*i+1]])        # [[2, 1], [2, 5]...]

    left = [0] * (e+2)      # 왼쪽 자식 저장할 리스트(노드가 e+1개 이므로 한칸씩 더 생성)
    right = [0] * (e+2)     # 오른쪽 자식 저장할 리스트

    for i in b:
        if left[i[0]] == 0:     # 왼쪽 자식의 해당 부모 인덱스 자리가 비어있다면
            left[i[0]] = i[1]   # 저장
        else:                   # 아니라면 오른쪽 자식에 저장
            right[i[0]] = i[1]

    print(f'#{tc} {preorder(n)}')

