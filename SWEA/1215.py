for tc in range(1, 11):

    n = int(input())
    a = []
    for i in range(0, 8):
        a.append(input())

# n = 4
# a = ['CBBCBAAB', 'CCCBABCB', 'CAAAACAB', 'BACCCCAC', 'AABCBBAC', 'ACAACABC', 'BCCBAABC', 'ABBBCCAA']

    cnt = 0
    row = 0
    a_2 = []

    # 가로 회문찾기
    for line in a:
        for index in range(len(line)-(n-1)):
            tmp = ''
            tmp = line[index:index+n]
            if tmp == tmp[::-1]:
                cnt += 1

    # 세로로 정렬
    while True:
        tmp_2 = ''
        for line in a:
            tmp_2 += line[row]
        a_2.append(tmp_2)
        row += 1
        if row == len(a[0]):
            break

    # 세로 회문찾기
    for line in a_2:
        for index in range(len(line)-(n-1)):
            tmp = ''
            tmp = line[index:index+n]
            if tmp == tmp[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')
