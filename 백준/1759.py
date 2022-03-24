def dfs(start):

    if len(rlt) == l:
        cnt = 0
        for i in rlt:
            if i in vowel:
                cnt += 1

        if cnt >= 1 and l-cnt >= 2:
            print(''.join(rlt))
            return
        else:
            return

    for j in range(start, c):
        if a[j] not in rlt:
            rlt.append(a[j])
            dfs(j+1)
            rlt.pop()


l, c = map(int, input().split())
a = list(input().split())
a = sorted(a)

vowel = ['a', 'e', 'i', 'o', 'u']
rlt = []
dfs(0)

