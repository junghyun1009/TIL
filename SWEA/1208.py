for tc in range(1, 11):

    n = int(input())
    a = list(map(int, input().split()))
    # n = 2
    # a = [5, 8, 3, 1, 5, 6, 9, 9, 2, 2, 4]

    for i in range(1, n+1):

        max_index = a.index(max(a))
        min_index = a.index(min(a))
        a[max_index] -= 1
        a[min_index] += 1

    print(f'#{tc} {max(a)-min(a)}')