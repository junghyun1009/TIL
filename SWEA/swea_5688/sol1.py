import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = int(input())        # 양의 정수
    i = 1

    while True:
        if i**3 > n:        # i의 세제곱이 n을 넘어가면 -1 저장하고 종료
            rlt = -1
            break

        if n % i == 0:      # n이 i로 나누어떨어지면
            divide = n / i      # 그 몫을 저장하고

            if divide == i**2:      # 그 값이 i의 제곱과 같다면 i를 저장하고 종료
                rlt = i
                break

        i += 1      # i를 1씩 증가시키며 확인

    print(f'#{tc} {rlt}')

