import sys

sys.stdin = open('input.txt')

def pel(a):
    if a == a[::-1]:
        return 1
    else:
        return 0

for tc in range(1, 11):
    n = int(input())
    a = [list(input()) for _ in range(100)]

    rlt_a = 0

    for l in range(100, 0, -1):
        if rlt_a != 0:
            break
        for i in a:
            if rlt_a != 0:
                break
            for idx in range(0, 101-l):
                tmp = i[idx:idx+l]
                if pel(tmp) == 1:
                    rlt_a = l
                    break


    b = []
    for c in range(100):
        tmp = []
        for r in range(100):
            tmp.append(a[r][c])
        b.append(tmp)

    rlt_b = 0

    for l in range(100, 0, -1):
        if rlt_b != 0:
            break
        for i in b:
            if rlt_b != 0:
                break
            for idx in range(0, 101 - l):
                tmp = i[idx:idx + l]
                if pel(tmp) == 1:
                    rlt_b = l
                    break

    print(f'#{tc} {max(rlt_a, rlt_b)}')

