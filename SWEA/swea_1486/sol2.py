import sys

sys.stdin = open('input.txt')

def dfs(s, num):
    if len(tmp) == num:
        rlt = tmp[:]
        # print(rlt)
        tall.append(rlt)
        return tall

    for i in range(s, n):
        if i not in idx:
            idx.append(i)
            tmp.append(h[i])
            dfs(i+1, num)
            idx.pop()
            tmp.pop()
    return        


T = int(input())

for tc in range(1, T + 1):

    n, b = map(int, input().split())
    h = list(map(int, input().split()))

    idx = []
    tmp = []
    rlt = []
    tall = []
    find_min = []
    
    for i in range(1, n+1):
        dfs(0, i)
    # print(tall)

    for j in tall:
        if sum(j) >= b:
            find_min.append(sum(j)-b)

    print(f'#{tc} {min(find_min)}')

