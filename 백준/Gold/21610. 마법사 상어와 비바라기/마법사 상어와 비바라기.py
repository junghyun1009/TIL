N, M = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(N)]
move = [list(map(int, input().split())) for _ in range(M)]

cloud = [[N-2, 0], [N-2, 1], [N-1, 0], [N-1, 1]]
# print(cloud)

for m in move:
    ground_org = [arr[:] for arr in ground]
    direction = m[0]
    cnt = m[1]

    dir_arr = [[0, 0], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
    
    # 1. 구름 이동
    distance = [dir_arr[direction][0]*cnt, dir_arr[direction][1]*cnt]
    cloud_moved = []
    for c in cloud:
        nr = c[0] + distance[0]
        nc = c[1] + distance[1]

        # 범위를 벗어나면 범위 안으로 들어오게
        while nr >= N:
            nr -= N
        while nr < 0:
            nr += N
        while nc >= N:
            nc -= N
        while nc < 0:
            nc += N

        cloud_moved.append([nr, nc])
        cloud = cloud_moved

    # 2. 구름이 있는 자리에 물 1 증가
    for c in cloud:
        ground[c[0]][c[1]] += 1

    # 3. 구름이 모두 사라짐
    cloud = []

    # 4. 물이 증가한 칸의 대각선에 물이 있는 칸의 수만큼 물 양 증가
    diagonal = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for cm in cloud_moved:
        cnt = 0
        for dia in range(4):
            dr = cm[0] + diagonal[dia][0]
            dc = cm[1] + diagonal[dia][1]

            if (0 <= dr < N) and (0 <= dc < N) and ground[dr][dc]:
                cnt += 1
        ground[cm[0]][cm[1]] += cnt

    # 5. 새로운 구름
    for row in range(N):
        for col in range(N):
            if (ground[row][col] >= 2) and (ground[row][col] == ground_org[row][col]):
                ground[row][col] -= 2
                cloud.append([row, col])

water = 0
for r in ground:
    for c in r:
        water += c

print(water)
        
    
