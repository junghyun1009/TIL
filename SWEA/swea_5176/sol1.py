import sys

sys.stdin = open('input.txt')


def inorder(v):
    '''
    중위 순회를 하며 1부터 차례로 채워나가고 있으므로 중위 순회 함수 사용
    :param v: 시작 노드
    :return: 중위 순회를 하며 읽은 노드 번호를 차례대로 저장한 리스트
    '''
    if v:
        inorder(left[v])
        order.append(v)     # print 대신 리스트에 해당 노드 번호 추가
        inorder(right[v])
    return order


T = int(input())

for tc in range(1, T + 1):

    n = int(input())        # 노드의 수
    left = [0] * (n+1)      # 왼쪽 자식 리스트
    right = [0] * (n+1)     # 오른쪽 자식 리스트
    order = [0]     # 후위 순회했을 때 읽히는 노드 번호 저장 리스트 (0번 인덱스는 비워둠)
                    # 인덱스와 해당 노드에 저장된 값을 일치시키기 위함

    for i in range(2, n + 1):       # 1번 노드는 부모가 없으므로 2번 노드부터
        if i % 2 == 0:      # 짝수 노드인 경우 왼쪽 자식의 부모 인덱스에 자기 노드 저장
            left[i//2] = i
        else:       # 홀수 노드인 경우 오른쪽 자식의 부모 인덱스에 자기 노드 저장
            right[i//2] = i

    order = inorder(1)      # 중위 순회하며 읽은 노드 번호 리스트 받아오기

    for j in range(n+1):
        if order[j] == 1:       # order에 저장된 노드 번호가 1이라면 그 때의 인덱스(=노드에 저장된 값) 저장
            a = j
        elif order[j] == n//2:      # order에 저장된 노드 번호가 n//2라면 그 때의 인덱스(=노드에 저장된 값) 저장
            b = j

    print(f'#{tc} {a} {b}')

