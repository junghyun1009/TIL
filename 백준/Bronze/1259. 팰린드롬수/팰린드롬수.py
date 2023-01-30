while True:
    num = input()
    reversed_num = num[::-1]

    if num == '0':
        break
    else:
        if num == reversed_num:
            print('yes')
        else:
            print('no')