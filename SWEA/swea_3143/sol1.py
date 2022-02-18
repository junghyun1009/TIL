import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):

    a, b = input().split()                  # a : 전체 문자열 / b : 자동완성 문자열

    idx = 0                                 # a의 인덱스를 확인할 변수
    cnt = 0                                 # 타이핑 수를 셀 변수

    while True:

        if idx == len(a):                   # 중단조건 : 인덱스가 a의 길이가 같아지면 중단
            break

        if a[idx] != b[0]:                  # a에서 한글자씩 확인할 때 b의 첫 글자와 다르다면
            idx += 1                        # 인덱스 하나 늘리고
            cnt += 1                        # 타이핑 수 하나 늘리기

        else:                               # a에서 한글자씩 확인할 때 b의 첫 글자와 같다면
            if a[idx:idx+len(b)] == b:      # 그 인덱스부터 b의 글자 수만큼 슬라이싱했을 때 b와 일치한다면
                idx += len(b)               # 인덱스를 b의 글자 수만큼 증가시키고
                cnt += 1                    # 타이핑 수 하나 늘리기

            else:                           # 슬라이싱한게 b와 다르다면
                idx += 1                    # 인덱스 하나 늘리고
                cnt += 1                    # 타이핑 수 하나 늘리기

    
    print(f'#{tc} {cnt}')

