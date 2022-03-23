import sys

sys.stdin = open('input.txt')


def findkey(a):     # 암호만 따로 저장하는 함수

    password = []       # 암호를 저장하기 위한 리스트

    for i in a:     # 받은 리스트의 각 행에 대해서
        if '1' in i:        # 1이 있는 행일 때
            for k in range(m - 1, -1, -1):      # 마지막 인덱스부터 확인
                if i[k] == '1':     # 1을 찾는다면
                    j = k       # 그 인덱스까지가 암호

                    while True:
                        if i[j - 6:j + 1] in num:       # 거꾸로 7칸씩 확인
                            b = i[j - 6:j + 1]
                            password.append(P.get(b))       # 암호를 숫자로 변경하여 리스트에 추가
                            j = j - 7       # 앞으로 7칸 이동

                        else:       # 해독할 수 없는 암호라면
                            return password     # 암호 끝, 반환


T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())

    a = [input() for _ in range(n)]
    P = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    k = findkey(a)      # 거꾸로 해독된 암호 저장
    password = k[::-1]      # 암호 배열 제대로 바꿔주기

    odd = 0
    even = 0

    for i in range(len(password) - 1):
        if (i + 1) % 2 == 0:        # 짝수번째 자리인 경우
            even += password[i]

        else:       # 홀수번째 자리인 경우
            odd += password[i]

    check = odd * 3 + even + password[-1]       # 암호 판정식 계산

    if check % 10 == 0:     # 10으로 나누어떨어진다면 암호가 맞으므로 각 자리의 합을 저장
        rlt = sum(password)

    else:       # 아니라면 0을 저장
        rlt = 0

    print(f'#{tc} {rlt}')

