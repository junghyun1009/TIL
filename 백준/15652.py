def dfs(start):
    if len(num) == m:
        print(*num)
        return

    for i in range(start, n+1):
        num.append(i)
        dfs(i)
        num.pop()

n, m = map(int, input().split())
num = []
dfs(1)