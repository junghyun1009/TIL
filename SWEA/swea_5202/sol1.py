import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N = int(input())        # 신청서 수
    SE = [list(map(int, input().split())) for _ in range(N)]        # 작업시간 리스트

    SE.sort(key=lambda x:x[1])      # 작업시간이 끝나는 시간 순서로 배열

    e = SE[-1][1]       # 가장 마지막 화물차의 작업이 끝나는 시간
    s = SE[-1][0]       # 가장 마지막 화물차가 작업을 시작하는 시간
    time = e - s        # 작업 시간
    cnt = 1     # 작업 횟수

    for i in range(N-1, -1, -1):        # 모든 화물차를 확인
        # 1. 범위가 겹치는 경우
        if s < SE[i][1] <= e:       # 저장되어 있는 작업 시작과 끝 시간 사이에 다음 화물차의 작업 끝 시간이 포함되면
            # 작업시간이 더 짧으면
            if SE[i][1] - SE[i][0] < time:
                # 그 스케줄로 갱신
                e = SE[i][1]        # 작업 끝 시간 갱신
                s = SE[i][0]        # 작업 시작 시간 갱신
                time = e - s        # 작업 시간 갱신(바꿔치기 한 것이므로 작업 횟수는 추가하지 않음)

        # 2. 범위가 안 겹치는 경우
        else:
            e = SE[i][1]
            s = SE[i][0]
            time = e - s
            cnt += 1        # 작업 횟수 추가

    print(f'#{tc} {cnt}')
