import sys

sys.stdin = open('input.txt')


def dfs(s, ssum):       # 모든 사무실을 돌아다니면서 배터리 소비량을 계산하기 위한 함수
    global msum

    if len(stack) == N:     # 스택에 사무실이 다 들어갔으면
        ssum += battery[s-1][0]     # 마지막 배터리 소모량 추가
        if msum > ssum:     # msum과 비교하며 최소 배터리 소모량 갱신
            msum = ssum
            return

    for i in range(1, N+1):     # 모든 사무실에 대해서
        if i not in stack:      # 스택에 없는 사무실이라면
            stack.append(i)     # 스택에 추가해주고
            dfs(i, ssum + battery[s-1][i-1])        # 추가해준 사무실에 대해 함수 실행, 배터리 소모량 더해서 넘겨줌
            stack.pop()     # 다음 경우를 위해서 스택에서 빼줌


T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    stack = [1]     # 1번 사무실부터 시작하므로 먼저 넣고 시작
    msum = 9999999      # 최소 배터리 소비량을 저장하기 위한 변수
    ssum = 0        # 배터리 소비량을 저장하기 위한 변수
    dfs(1, ssum)
    
    print(f'#{tc} {msum}')

