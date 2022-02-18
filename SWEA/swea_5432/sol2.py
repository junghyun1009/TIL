import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a = input()

    number = a.replace('()', '1')
    a_num = len(number)
    cnt = 0
    rlt = 0

    for i in number:
        if i == '(':
            cnt += 1

        elif i == '1':
            rlt += cnt

        else:
            cnt += 1

    print(f'#{tc} {rlt}')

