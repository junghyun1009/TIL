import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m, l = map(int, input().split())     # n : 노드의 수, m : 리프 노드의 수, l : 값을 출력할 노드 번호
    a = [list(map(int, input().split())) for _ in range(m)]     # a에 리프 노드의 정보 저장
    # a = [[4, 1], [5, 2], [3, 3]] <- [노드 번호, 값]의 묶음

    tree = [0] * (n+1)      # 각 노드의 값을 저장할 트리(인덱스와 노드 번호를 안 헷갈리게 하기 위해 n+1칸으로 생성)

    for i in a:
        tree[i[0]] = i[1]       # 갖고 있는 리프 노드의 정보를 트리에 저장

    for j in range(n, 1, -1):       # 리프 노드부터 시작해야하므로 가장 마지막 노드에서부터 시작
        tree[j//2] += tree[j]       # 부모 노드에 자기 자신을 더해줌

    print(f'#{tc} {tree[l]}')

