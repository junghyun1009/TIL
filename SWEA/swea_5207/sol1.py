import sys

sys.stdin = open('input.txt')


def bins(A, N, t):      # A:타겟을 찾고자하는 배열, N:배열의 크기, t:타겟

    start = 0       # 탐색 시작 인덱스
    end = N - 1     # 탐색 끝 인덱스

    while start <= end :
        middle = (start + end) // 2     # 중앙 인덱스

        if A[middle] == t:      # 중앙값이 타겟과 같다면 True 반환
            return True
        elif A[middle] > t:     # 중앙값이 타겟보다 크다면 왼쪽 탐색
            end = middle - 1
            rlt.append(1)       # 왼쪽 탐색인 것을 표시하기 위해 1 남기기
        else:       # 중앙값이 타겟보다 작다면 오른쪽 탐색
            start = middle + 1
            rlt.append(2)       # 오른쪽 탐색인 것을 표시하기 위해 2 남기기
            
    return False        # 탐색 실패했으면 False 반환


T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cnt = 0     # 조건을 만족하는 타겟의 수를 세기 위한 변수
    A = sorted(A)       # 이진탐색을 하려면 정렬되어 있어야 함

    for b in B:     # B의 각각의 원소에 대해서
        rlt = []
        if bins(A, N, b):       # 타겟이 있다면
            if len(rlt) <= 1:       # 두번 이내에 찾은 경우(좌우 왔다갔다 안해도 돼서 조건 만족)
                cnt += 1
            else:
                # 1. 모든 짝수인덱스는 1, 홀수인덱스는 2인 경우
                if rlt[0] == 1:
                    flag = 1        # 정상 종료됐다면 flag에 1 반환될 것
                    for r in range(len(rlt)):
                        if r % 2 == 0 and rlt[r] == 1:
                            continue
                        elif r % 2 == 1 and rlt[r] == 2:
                            continue
                        else:
                            flag = 0        # 비정상 종료
                            break

                    if flag == 1:       # 정상 종료 되었을 경우 cnt 추가
                        cnt += 1

                # 모든 짝수인덱스는 2, 홀수인덱스는 1인 경우
                else:
                    flag = 1
                    for r in range(len(rlt)):
                        if r % 2 == 0 and rlt[r] == 2:
                            continue
                        elif r % 2 == 1 and rlt[r] == 1:
                            continue
                        else:
                            flag = 0
                            break

                    if flag == 1:
                        cnt += 1

    print(f'#{tc} {cnt}')

