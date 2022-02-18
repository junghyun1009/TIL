import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a = input()                         # 찾고 싶은 문자열
    b = input()                         # 전체 문자열

    num_list = []                       # 각 문자의 개수를 저장할 리스트

    for word_a in a:
        cnt = 0                         # 각 문자의 개수를 셀 변수
        for word_b in b:
            if word_a == word_b:        # a의 각 문자를 b의 각 문자와 같은지 확인하고, 같다면 개수 1 추가
                cnt += 1
        num_list.append(cnt)            # num_list에 각 문자의 개수에 대한 정보 추가

    max_num = num_list[0]               # num_list에서 max 찾기

    for number in num_list:
        if number > max_num:
            max_num = number

    print(f'#{tc} {max_num}')

