import sys

sys.stdin = open('input.txt')


def babygin(a):     # 리스트 내에 babygin이 있는지 확인하기 위한 함수
    # 1. run(연속 숫자의 경우)
    for i in range(8):
        check = a[i:i+3]        # 세개씩 슬라이싱
        if check[0] >= 1 and check[1] >= 1 and check[2] >= 1:       # 각각 1개 이상 있으면
            return True     # babygin!

    # 2. triplet(같은 숫자가 세개 있는 경우)
    for j in range(10):
        if a[j] == 3:       # 3개라면
            return True     # babygin!

    return False        # 두 경우 모두 아니라면 babygin 아님


T = int(input())

for tc in range(1, T + 1):

    card = list(map(int, input().split()))

    one = [0] * 10      # 1번 선수가 갖고 있는 카드 목록
    two = [0] * 10      # 2번 선수가 갖고 있는 카드 목록
    winner = 0      # 무승부인 경우를 위해 0 저장해놓기

    for i in range(12):
        if i % 2 == 0:      # 인덱스가 짝수이면 1번 선수 카드
            one[card[i]] += 1       # 카드 목록에 추가
            if babygin(one):        # babygin 있는지 확인
                winner = 1      # 있으면 우승자는 1번, 끝
                break

        else:       # 인덱스가 홀수이면 2번 선수 카드
            two[card[i]] += 1       # 카드 목록에 추가
            if babygin(two):        # babygin 있는지 확인
                winner = 2      # 있으면 우승자는 2번, 끝
                break

    print(f'#{tc} {winner}')

