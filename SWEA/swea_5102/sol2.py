import sys

sys.stdin = open('input.txt')


def bfs(s, g):      # 연결 경로를 탐색하기 위한 함수

    queue = []      # 다음 목적지를 확인하기 위한 큐

    for j in a:
        if j[0] == s and j[1] != g:     # 주어진 리스트에 대해서 출발점이 같은 간선 정보 찾기
            queue.append(j)     # 큐에 추가
            visited[j[0]][j[1]] = 1     # 방문 표시(쌍방)
            visited[j[1]][j[0]] = 1

        elif j == [s, g]:       # 출발 노드와 도착 노드가 간선 하나로 연결되면 바로 1 반환
            return 1

    while queue:        # 큐가 빌 때까지
        now = queue.pop(0)      # 현재 노드는 큐의 첫번째 요소

        for i in range(51):     # 다음 간선 찾기
            if graph[now[1]][i] == 1 and visited[now[1]][i] == 0:       # 그래프에서 1로 표시되어있고, 아직 방문을 안 했다면
                queue.append([now[1], i])       # 큐에 추가
                visited[now[1]][i] = visited[now[0]][now[1]] + 1        # 이동 거리를 알기 위해서 이전 방문 표시한 수보다 1 증가시켜서 저장(쌍방)
                visited[i][now[1]] = visited[now[1]][i]

                if i == g:      # 도착 노드에 도달했다면
                    return visited[now[1]][i]       # 이동 거리 반환

    return 0        # 큐가 빌 때까지 반환을 못했다면 경로가 없는 것이므로 0 반환


T = int(input())

for tc in range(1, T + 1):

    v, e = map(int, input().split())        # v:노드 수, e:간선 수
    a = [list(map(int, input().split())) for _ in range(e)]     # 간선 정보
    s, g = map(int, input().split())        # s:출발 노드, g:도착 노드

    graph = [[0] * 51 for _ in range(51)]       # 각 요소마다 연결 여부를 나타낼 그래프
    visited = [[0] * 51 for _ in range(51)]     # 경로를 탐색하며 방문 표시를 할 2차원 리스트

    for i in a:
        graph[i[0]][i[1]] = 1       # 방향성이 없는 간선이므로 양쪽 다 연결 표시
        graph[i[1]][i[0]] = 1

    print(f'#{tc} {bfs(s, g)}')

