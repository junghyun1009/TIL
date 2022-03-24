import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, m = map(int, input().split())        # n:배열 세로, m:배열 가로
    a = [input() for _ in range(n)]
    hexlist = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
           '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
           'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
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
    binary = ''
    odd = []
    even = []

    for i in a:
        if i != '0' * m:
            target = i
            break

    for j in target:
        binary += hexlist.get(j)

    for k in range(len(binary)-1, -1, -1):
        if binary[k] == '1':
            idx = k
            break

    # print(idx)

    i = 1
    while True:
        password = binary[idx-56*i+1:idx+1]
        if '1' in binary[0:idx-56*i+1]:
            i = i + 1
        else:
            break

    for cnt in range(1, 9):
        if cnt % 2 == 1:
            cut = ''
            each = password[7 * i * (cnt - 1):7 * i * cnt]
            for j in range(0, len(each), i):
                cut += each[j]
            odd.append(P.get(cut))
        else:
            cut = ''
            each = password[7 * i * (cnt - 1):7 * i * cnt]
            for j in range(0, len(each), i):
                cut += each[j]
            even.append(P.get(cut))

    cal = sum(odd) * 3 + sum(even)

    if cal % 10 == 0:
        rlt = sum(odd) + sum(even)
    else:
        rlt = 0

    # print(target)
    # print(binary)
    # print(password)
    # print(odd)
    # print(even)
    print(f'#{tc} {rlt}')

