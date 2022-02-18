import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    n, m = map(int, input().split())                    # n : 가로, 세로 문자열의 길이 / m : 찾고 싶은 회문의 길이
    a = []                                              # a라는 리스트에 각 줄의 문자열을 글자 단위로 나누어 저장
    for i in range(n):
        a.append(list(input()))

    # 가로 회문 찾기
    for row_idx in range(len(a)):
        for word in range(len(a[row_idx])-(m-1)):       # 찾으려는 회문의 길이만큼 슬라이싱
            slice = a[row_idx][word : word + m]

        if slice == slice[::-1]:                        # 슬라이싱한 것과 뒤집은 것이 일치한다면 rlt에 저장
            rlt = slice

    # 행렬 돌리기
    b = []                                              # 문자열 리스트 돌리기
    for col_idx in range(len(a[0])):
        tmp = []
        for row_idx in range(len(a)):
            tmp.append(a[row_idx][col_idx])
        b.append(tmp)

    # 세로 회문 찾기
    for row_idx in range(len(b)):
        for word in range(len(a[row_idx])-(m-1)):       # 찾으려는 회문의 길이만큼 슬라이싱
            slice = b[row_idx][word : word + m]

        if slice == slice[::-1]:                        # 슬라이싱한 것과 뒤집은 것이 일치한다면 rlt에 저장
            rlt = slice


    print(f'#{tc}', end=" ")

    for word in rlt:
        print(f'{word}', end="")

    print()


