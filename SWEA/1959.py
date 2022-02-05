t = int(input())

for tc in range(1, 11):
    tmp = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a = [1, 5, 3]
    # b = [3, 6, -7, 5, 4]
    sum_list = []

    if len(a) <= len(b):
        for i in range(len(b)-len(a)+1):
            mul_list = []
            for idx in range(len(a)):
                mul_list.append(a[idx]*b[idx+i])
            sum_list.append(sum(mul_list))

    else:
        for i in range(len(a)-len(b)+1):
            mul_list = []
            for idx in range(len(b)):
                mul_list.append(b[idx]*a[idx+i])
            sum_list.append(sum(mul_list))

    print(f'#{tc} {max(sum_list)}')