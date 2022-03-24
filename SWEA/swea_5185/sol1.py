import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, num = input().split()        # n:자릿수, num:16진수 숫자

    n = int(n)      # 정수로 형 변환
    hex = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}        # 알파벳으로 표시되는 16진수와 10진수 숫자 매칭
    alph = ['A', 'B', 'C', 'D', 'E', 'F']
    dec = 0     # 16진수를 10진수로 변환하여 나타낼 변수
    bin = 0     # 10진수를 2진수로 변환하여 나타낼 변수
    cnt = -1        # 2진수 계산할 때 자릿수 계산을 위한 변수

    for i in range(n-1, -1, -1):        # 16진수 -> 10진수(맨 뒤부터 차례로 변환)
        if num[i] in alph:      # 알파벳인 경우, 딕셔너리 값 사용
            dec += hex.get(num[i]) * (16**(n-i-1))
        else:       # 숫자인 경우, 정수로 형 변환하여 사용
            dec += int(num[i]) * (16**(n-i-1))

    while True:     # 10진수 -> 2진수(2로 나누어가며 몫과 나머지 사용)
        if dec == 1:        # 숫자가 1로 갱신된다면
            bin += 10 ** (cnt+1)        # 알맞은 자리에 마지막으로 넣어주고 중단
            break

        q = dec % 2     # 2로 나눈 나머지
        dec = dec // 2      # 2로 나눈 몫으로 갱신
        cnt += 1        # 자릿수 계산
        bin += q * (10**cnt)        # 뒤에서부터 앞으로 써나가기

    rlt = '0' * (n*4 - len(str(bin))) + str(bin)        # 비어있는 자리는 0으로 채우기 위함

    print(f'#{tc} {rlt}')

