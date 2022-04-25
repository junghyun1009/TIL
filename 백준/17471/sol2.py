def dfs(s, tmp_a, num):
    if len(tmp_a) == num:
        tmp_b = []
        for i in range(1, N + 1):
            if visited[i] == 0:
                tmp_b.append(i)
        print(tmp_a)
        print(tmp_b)
        return

    for i in range(s, N + 1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i+1, tmp_a + [i], num)
            visited[i] = 0


N = 6
visited = [0] * (N + 1)
tmp_a = []
dfs(1, tmp_a, 2)