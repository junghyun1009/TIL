def dfs(tmp):
    if len(tmp) == N:
        print(*tmp)
        return

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(tmp + [i])
            visited[i] = 0

N = int(input())
visited = [0] * (N+1)
dfs([])