import sys

sys.stdin = open('input.txt')

T = int(input())

def push(a, b):
    a.append(b)

def pop(a):
    if len(a) == 0:
        return 0

    else:
        return a.pop(-1)

for tc in range(1, T + 1):

    a = input()
    b = []
    end = ''

    for i in a:
        if i == '(':
            push(b, '(')

        elif i == ')' and len(b) == 0:
            end = ')'
            break

        else:
            pop(b)

    if len(b) > 0:
        print('NO')

    elif end == ')' and len(b) == 0:
        print('NO')

    else:
        print('YES')



