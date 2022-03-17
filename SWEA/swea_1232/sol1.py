import sys

sys.stdin = open('input.txt')


def postorder(v):
    '''
    가장 root에 있는 연산자를 가장 나중에 처리해야하므로 후위 순회 함수 사용
    :param v: root 노드
    :return: 계산하는 순서대로 나열한 리스트
    '''
    if v:
        postorder(left[v])
        postorder(right[v])
        calculate.append(tree[v])   # print 대신 calculate에 해당 노드에 있는 값 저장

    return calculate


for tc in range(1, 11):

    n = int(input())    # 정점의 총 수
    a = [list(input().split()) for _ in range(n)]   # 트리 정보 저장

    left = [0] * (n+1)      # 왼쪽 자식 리스트
    right = [0] * (n+1)     # 오른쪽 자식 리스트
    tree = [0] * (n+1)      # 각 노드의 값이 저장되는 트리
    calculate = []      # 연산 순서대로 나열할 리스트

    for i in a:
        # 연산자 노드인 경우
        if len(i) == 4:
            tree[int(i[0])] = i[1]      # 트리의 해당 노드에 연산자 저장
            left[int(i[0])] = int(i[2])     # 왼쪽 자식 리스트의 부모 인덱스에 노드 번호 저장
            right[int(i[0])] = int(i[3])    # 오른쪽 자식 리스트의 부모 인덱스에 노드 번호 저장

        # 아닌 경우
        else:
            tree[int(i[0])] = int(i[1])     # 트리의 해당 노드에 숫자 저장

    calculate = postorder(1)        # 후위 순회하며 연산 순서대로 나열한 리스트 받아오기

    stack = []      # 후위연산식을 계산하기 위한 스택
    cal = ['+', '-', '*', '/']      # 연산자 목록

    for i in calculate:
        if i not in cal:        # 연산자가 아니라면
            stack.append(i)     # 스택에 푸시

        else:       # 연산자라면
            n2 = stack.pop()        # 스택에서 두번 팝
            n1 = stack.pop()
            if i == '+':
                stack.append(n1+n2)
            elif i == '-':
                stack.append(n1-n2)
            elif i == '*':
                stack.append(n1*n2)
            else:
                stack.append(n1/n2)

    rlt = stack[0]      # 마지막에는 결과값만 남아있는 상태

    print(f'#{tc} {int(rlt)}')

