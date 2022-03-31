import sys

sys.stdin = open('input.txt')


def dfs(s, p, c):       # 최소 충전 횟수를 반환하기 위한 함수
    global charge

    if charge <= c:     # 이미 저장된 횟수 이상 충전한 경우 중단
        return

    if s == bus - 2 and p >= 1:     # 종점 직전 정류장에 도달했는데 배터리가 1 이상 있으면
        if charge > c:      # 최솟값 갱신
            charge = c
            return

    elif p >= bus - 1 - s:      # 남아있는 거리를 해당 배터리로 갈 수 있으면
        if charge > c:      # 최솟값 갱신
            charge = c
        return

    for i in range(s, bus-1):       # 다음 버스 정류장을 순회하며
        if visited[i] == 0 and i - s <= battery[s]:     # 방문하지 않았고 갖고 있는 배터리로 그 정류장을 갈 수 있으면
            visited[i] = 1      # 방문 표시
            dfs(i, battery[i], c + 1)       # 해당 정류장에서 dfs 진행
            visited[i] = 0      # 복원


T = int(input())

for tc in range(1, T + 1):

    info = list(map(int, input().split()))

    bus = info[0]       # 버스 정류장 수
    battery = info[1:]      # 각 정류장에 있는 배터리 정보

    visited = [0] * bus     # 방문 정보 표시 리스트
    visited[0] = 1      # 첫번째 정류장 방문 표시
    power = battery[0]      # 첫번째 정류장 배터리 저장
    charge = 999999     # 최솟값 찾기 위한 변수
    dfs(0, power, 0)
    
    print(f'#{tc} {charge}')

