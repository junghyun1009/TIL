import sys
input = sys.stdin.readline

M = int(input())
S = 0b000000000000000000000

for _ in range(M):
    # print(_)
    cal = input()
    # 1. all
    if cal[0:3] == 'all':
        S = 0b111111111111111111110
        # print(bin(S))
    # 2. empty
    elif cal[0:5] == 'empty':
        S = 0b000000000000000000000
        # print(bin(S))

    else:
        c = list(cal.split(' '))
        # 1. add
        if c[0] == 'add':
            target = int(c[1])
            S = S | (1 << target)
            # print(bin(S))
        # 2. remove
        elif c[0] == 'remove':
            target = int(c[1])
            S = S & ~(1 << target)
            # print(bin(S))
        # 3. check
        elif c[0] == 'check':
            target = int(c[1])
            check = S & (1 << target)
            if check:
                print(1)
            else:
                print(0)
        # 4. toggle
        elif c[0] == 'toggle':
            target = int(c[1])
            S = S ^ (1 << target)
            # print(bin(S))
