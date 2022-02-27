import sys

sys.stdin = open('input.txt')

n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    list_a = [[1, 0], [2, 0], [3, 0], [4, 0]]
    list_b = [[1, 0], [2, 0], [3, 0], [4, 0]]

    for j in range(1, len(a)):
        for num in range(1, 5):
            if a[j] == num:
                list_a[num-1][1] += 1

    for k in range(1, len(b)):
        for num in range(1, 5):
            if b[k] == num:
                list_b[num-1][1] += 1

    idx = 3
    while True:
        if idx == -1:
            rlt = 'D'
            break

        if list_a[idx][1] > list_b[idx][1]:
            rlt = 'A'
            break

        elif list_a[idx][1] < list_b[idx][1]:
            rlt = 'B'
            break

        else:
            idx -= 1

    print(rlt)

