import sys

sys.stdin = open('input.txt')


def part(arr, start, end):      # pivot을 기준으로 왼쪽, 오른쪽 정렬을 하고 pivot의 인덱스를 반환하는 함수

    pivot = arr[start]
    left = start + 1
    right = end
    done = False

    while not done:

        while left <= right and pivot >= arr[left]:     # 왼쪽에는 pivot보다 작은 수
            left += 1
        while left <= right and pivot <= arr[right]:        # 오른쪽에는 pivot보다 큰 수
            right -= 1

        if left > right:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]       # 조건을 만족하지 않으면 두 수의 자리를 바꾸어줌

    arr[start], arr[right] = arr[right], arr[start]     # pivot을 크기에 맞는 인덱스로 보내기

    return right


def qsort(arr, start, end):

    if start < end:
        pivot = part(arr, start, end)       # pivot 불러오기
        qsort(arr, start, pivot-1)      # 왼쪽 퀵 소트
        qsort(arr, pivot+1, end)        # 오른쪽 퀵 소트
    return arr


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    nums = list(map(int, input().split()))
    A = qsort(nums, 0, N - 1)
    
    print(f'#{tc} {A[N//2]}')

