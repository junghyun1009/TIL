def dfs(arr, k, n):
    global archery

    if len(arr) == 3:
        archery.append(arr)
        return

    for i in range(k+1, n):
        dfs(arr+[i], i, n)
        

N, M, D = map(int, input().split())
castle = [list(map(int, input().split())) for _ in range(N)]
castle_org = [arr[:] for arr in castle]

# 적의 수, 위치
enemy_cnt = 0
enemy = []
rlt_list = []
for row in range(N):
    for col in range(M):
        enemy_cnt += castle[row][col]
        if castle[row][col] == 1:
            enemy.append([row, col])

enemy_org = [arr[:] for arr in enemy]
enemy_cnt_org = enemy_cnt

# 2 세개와 0을 정렬하는 순열 -> 2를 배치할 인덱스 세개 뽑기(조합)
archery = []
dfs([], -1, M)
# print(archery)

# 맨 마지막 줄에 궁수 추가해주기
for each in archery:
    rlt = 0
    castle = [arr[:] for arr in castle_org]
    castle.append([0] * M)
    enemy = [arr[:] for arr in enemy_org]
    enemy_cnt = enemy_cnt_org
    last = [0] * M
    archery_idx = []
    for idx in each:
        last[idx] = 2
        archery_idx.append([N, idx])
    castle[-1] = last
    # print(archery_idx)
    # print(castle)

    # 모든 적이 사라질 때까지 궁수가 공격하는 적의 수 세기
    while enemy_cnt:
        target = []
        for a in archery_idx:
            possible = []
            for e in enemy:
                distance = abs(a[0]-e[0]) + abs(a[1]-e[1])
                if distance <= D:
                    possible.append([distance, e[0], e[1]])
            order = sorted(possible, key=lambda x : (x[0], x[2]))
            if order:
                target.append([order[0][1], order[0][2]])
        target = list(set([tuple(item) for item in target]))
        # print(target)
        for t in target:
            castle[t[0]][t[1]] = 0
            enemy.remove([t[0], t[1]])
        # enemy_cnt -= len(target)
        rlt += len(target)

        # 적들 한칸씩 아래로 내려주기
        move_enemy = []
        for e in enemy:
            if 0 <= (e[0]+1) < N:
                move_enemy.append([e[0]+1, e[1]])
        enemy = [arr[:] for arr in move_enemy]
        enemy_cnt = len(enemy)
        castle.pop(-2)
        castle.insert(0, [0]*M)
        # print('111', castle)
        # print('222', enemy)

    rlt_list.append(rlt)

# print(rlt_list)
print(max(rlt_list))
    
