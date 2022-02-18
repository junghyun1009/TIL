import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a = input()

    idx = 0
    number = a.replace('()','1')
    a_num = len(number)

    # while True:
    #
    #     if idx == len(a):
    #         break
    #
    #     if a[idx] == '(' and a[idx+1] == ')':
    #         number.append(1)
    #         idx += 2
    #
    #     else:
    #         if a[idx] == '(':
    #             number.append(2)
    #             idx += 1
    #
    #         else:
    #             number.append(3)
    #             idx += 1
    #print(number)

    num_idx = 0
    cnt = 0
    cnt_2 = 0
    cnt_3 = 0
    idx_2 = -1
    #stick = ''
    sticks = ''

    while True:

        if cnt == a_num:
            break

        for num_idx in range(idx_2+1, a_num):
            if cnt == a_num:
                break

            if number[num_idx] == '(':
                if cnt_2 == 0:
                    cnt += 1
                    cnt_2 += 1
                    idx_2 = num_idx
                    #print(f'#1: {cnt}, {cnt_2}, {idx_2}')

                else:
                    cnt += 1
                    cnt_2 += 1
                    #print(f'#2: {cnt}, {cnt_2}')

            elif number[num_idx] == ')' and cnt_2 != 0:
                cnt += 1
                cnt_3 += 1
                idx_3 = num_idx
                #print(f'#3: {cnt}, {cnt_3}, {idx_3}')

            else:
                cnt += 1
                #print(f'#4: {cnt}')

            if cnt_2 != 0 and cnt_2 == cnt_3 and idx_2 < idx_3:
                #stick = number[idx_2:idx_3+1]
                #sticks = sticks + number[idx_2:idx_3+1] + '*'
                cnt = 0
                cnt_2 = 0
                cnt_3 = 0

                #print(stick)
                break

    print(sticks)
    rlt = 0
    #
    # for num in sticks:
    #     rlt += num.count('1') + 1
    #rlt = sticks.count('1') + sticks.count('*')

    for i in sticks:
        if i == '*' or i == '1':
            rlt += 1

    print(f'#{tc} {rlt}')

