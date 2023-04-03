N, M = map(int, input().split(' '))
visited = [0] * (N+1)

def dfs(arr, n, m):
    if len(arr) == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(arr+[i], n, m)
            visited[i] = 0

dfs([], N, M)