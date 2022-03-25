import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n, m, k = map(int, input().split())
    germs = [list(map(int, input().split())) for _ in range(k)]

    # 일단 미생물 처음 위치 저장
    # 상, 하, 좌, 우에에 맞게 델타 설정
    # bfs (동시에 이동하니까)
    # 근데 얘는 영역 표시하면서 다니면 안될 것 같음
    # 테두리에 닿으면 절반으로 바꾸고 반대방향
    # 여러 군집이 합쳐졌을 때 방향 설정

    print(f'#{tc} ')

