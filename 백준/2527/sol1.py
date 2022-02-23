import sys

sys.stdin = open('input.txt')

for i in range(4):

    a = list(map(int, input().split()))

    s1 = []
    s2 = []

    for i in range(0, 3, 2):
        for j in range(1, 4, 2):
            tmp = [a[i], a[j]]
            s1.append(tmp)

    for i in range(4, 7, 2):
        for j in range(5, 8, 2):
            tmp = [a[i], a[j]]
            s2.append(tmp)

    # print(s1)
    # print(s2)

    for i in range(4):

        for j in range(4):

            if s1[i] == s2[j]:
                rlt = 'c'
                break

            elif (s1[i][0] == s2[j][0]) or (s1[i][1] == s2[j][1]):
                if (i == 2 or i == 3) and (j == 0 or j == 1):
                    rlt = 'b'
                    break

                elif (i == 0 or i == 1) and (j == 2 or j == 3):
                    rlt = 'b'
                    break

            elif (s1[-1][0] < s2[0][0]) or (s1[0][0] > s2[-1][0]):
                rlt = 'd'

            elif (s1[-1][1] < s2[0][1]) or (s1[0][1] > s2[-1][1]):
                rlt = 'd'

            else:
                rlt = 'a'

        if rlt != 'a':
            break

    print(rlt)
