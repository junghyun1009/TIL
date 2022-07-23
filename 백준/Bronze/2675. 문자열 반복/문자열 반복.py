T = int(input())

for tc in range(1, T + 1):
    R, S = input().split()

    R = int(R)

    for i in S:
        print(i * R, end='')

    print()