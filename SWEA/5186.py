T = int(input())

for tc in range(1, T+1):

    n = float(input())

    bin = ''        # 2진수를 저장할 빈 문자열
    cnt = -1        # 자릿수를 위한 변수

    while True:
        if len(bin) == 13:      # 이진수가 13자리가 되면 overflow
            bin = 'overflow'
            break

        if n == 0:      # 더 이상 변환할 숫자가 없으면 중단
            break

        d = n // (2**cnt)       # 2**-1 부터 차례로 나누면서 몫을 문자열에 더해나감
        bin += str(int(d))
        n = n - d * (2**cnt)        # 변환하고 남은 숫자 계산
        cnt -= 1        # 자릿수 한칸 뒤로
        # print(n)

    print(f'#{tc} {bin}')