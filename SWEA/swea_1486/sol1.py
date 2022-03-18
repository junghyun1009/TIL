import sys
from itertools import combinations

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    subset = []     # 모든 부분집합을 저장할 리스트
    each_sub = []       # 각 부분집합의 합을 저장할 리스트

    for i in range(1, n+1):
        subset.append(list(combinations(a, i)))     # 원소의 개수가 1~n인 모든 부분집합을 저장

    for j in subset:
        for k in j:
            if sum(k) >= b:     # 부분집합의 합이 b보다 클 때
                each_sub.append(sum(k)-b)     # 부분집합의 합에서 b를 뺀 값을 저장

    # print(subset)
    # print(each_sub)
    print(f'#{tc} {min(each_sub)}')     # 그 차이가 가장 작을 때 출력

