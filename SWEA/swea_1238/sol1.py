import sys
from collections import deque

sys.stdin = open('input.txt')


def bfs(a):
    queue = deque()
    queue.append(a)     # 맨 처음 사람 먼저 넣어주기
    visited[a] = 1      # 방문 표시

    while queue:    # 큐가 다 빌 때까지
        now = queue.popleft()       # 가장 앞에 들어있는 요소 빼서 저장
        for i in range(1, 101):
            if graph[now][i] == 1 and visited[i] == 0:      # 그래프의 해당 행을 순회하며 1을 가진 열(연락한 대상)이면서 방문하지 않았다면
                queue.append(i)     # 큐에 넣어준다
                visited[i] = visited[now] + 1       # 몇번째 방문인지 알기 위해서 이전 방문 횟수에 1을 더해서 저장

    return visited


for tc in range(1, 11):

    n, s = map(int, input().split())    # n:데이터의 길이, s:시작점
    contact = list(map(int, input().split()))   # 연락에 대한 정보
    pair = []   # 두개씩 묶어서 저장할 리스트
    graph = [[0] * 101 for _ in range(101)]   # 1번부터 100번까지 있으니까 101칸 만들어두기
    visited = [0] * 101     # 방문표시 및 몇번째 방문인지 기록할 리스트
    rlt = []    # 마지막 방문 대상을 저장할 리스트

    for i in range(0, n, 2):    # from-to 관계로 묶어주기
        pair.append([contact[i], contact[i+1]])

    for i in pair:  # 그래프 만들어주기(연락한 사람의 row, 연락 받은 사람의 col에 1 저장)
        graph[i[0]][i[1]] = 1

    visited = bfs(s)

    find_max = max(visited)     # 마지막 방문 번째를 알기 위해 최댓값 찾기
    for i in range(101):
        if visited[i] == find_max:      # 해당 번째를 가진 인덱스를 저장
            rlt.append(i)

    print(f'#{tc} {max(rlt)}')

