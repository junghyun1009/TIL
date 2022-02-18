import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a = []                              # 문자열 한줄을 하나의 원소로 저장할 리스트

    for _ in range(5):
        a.append(input())

    length = []                         # 각 문자열의 길이를 저장할 리스트
    rlt = ""                            # 최종 문자열을 출력할 변수

    for word in a:                      # 최대 문자열의 길이에 맞춰 출력해야하므로
        length.append(len(word))        # 각각의 문자열의 길이를 저장

    max_len = length[0]
    
    for word_len in length:             # 최대 문자열의 길이 구하기
        if word_len >= max_len:
            max_len = word_len

    for col in range(max_len):          # 최대 문자열의 길이에 맞추어
        for row in range(5):            # 세로로 읽기

            if len(a[row]) >= col+1:    # 인덱스 범위 안에 들어가면 rlt에 문자 추가
                rlt += a[row][col]
            else:                       # 안 들어가면 ''추가
                rlt += ''


    print(f'#{tc} {rlt}')

