def dfs():
    if len(num) == m:
        print(*num)
        return

    for i in range(1, n+1):
        if i not in num and num[-1] < i:
            num.append(i)
            dfs()
            num.pop()


n, m = map(int, input().split())

for i in range(1, n+1):
    num = [i]
    dfs()