import sys

sys.stdin = open('input.txt')

# 최대 회문 길이 찾기 함수
def find_max(a):

    for length in range(len(a[0]),0,-1):                    # 회문 판별 길이를 가장 긴 것부터 줄여나가며 확인
        for row in a:
            for col in range(len(row)-(length-1)):          # a의 각 행에 대해서 해당 길이만큼 슬라이싱하여
                tmp = row[col:col+length]

                if tmp == tmp[::-1]:                        # 뒤집어도 똑같은지 확인하고, 똑같다면
                    return length                           # 그 때의 length 반환


for tc in range(1, 11):

    n = int(input())
    a = []
    for i in range(100):
        a.append(list(input()))


    # 행렬 돌리기
    b = []

    for col in range(len(a[0])):
        tmp_b = []
        for row in range(len(a)):
            tmp_b.append(a[row][col])
        b.append(tmp_b)


    max_a = find_max(a)                                     # 원래 행렬에서 회문의 최대 길이 찾기
    max_b = find_max(b)                                     # 세로로 읽은 행렬에서 회문의 최대 길이 찾기

    if max_a >= max_b:                                      # 둘 중 최대 출력
        print(f'#{tc} {max_a}')

    else:
        print(f'#{tc} {max_b}')
