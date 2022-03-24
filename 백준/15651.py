def dfs():
    if len(num) == m:
        print(*num)
        return

    for i in range(1, n+1):
        num.append(i)
        dfs()
        num.pop()

n, m = map(int, input().split())
num = []
dfs()