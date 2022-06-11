def dfs(tmp):
    if len(rlt) == 1:
        return

    if 3 <= len(tmp) <= N:
        
        for j in range(2, len(tmp)):
            for k in range(len(tmp)-j):
                a = tmp[k:k+j]
                b = tmp[k+j:k+2*j]
                if a == b:
                    return

        if len(tmp) == N:
            rlt.append(tmp)
            return

    for i in range(1, 4):
        if len(tmp) > 0 and (tmp[-1] != str(i)):
            dfs(tmp + str(i))
        elif len(tmp) == 0:
            dfs(tmp + str(i))

N = int(input())

rlt = []
dfs('')
print(rlt[0])