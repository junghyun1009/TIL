import sys

sys.stdin = open('input.txt')


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
    j = m - 1
    password = []


    def key(a):
        for i in a:
            if '1' in i:
                for k in range(m - 1, -1, -1):
                    if i[k] == '1':
                        j = k

                        while True:
                            if i[j - 6:j + 1] in num:
                                b = i[j - 6:j + 1]
                                password.append(P.get(b))
                                j = j - 7
                            else:
                                return password

    key = key(a)
    password = key[::-1]

    odd = 0
    even = 0

    for i in range(len(password)-1):
        if (i+1) % 2 == 0:
            even += password[i]
        else:
            odd += password[i]

    check = odd * 3 + even + password[-1]
    # print(password)
    # print(odd)
    # print(even)
    # print(check)

    if check % 10 == 0:
        rlt = sum(password)
    else:
        rlt = 0
    
    print(f'#{tc} {rlt}')

