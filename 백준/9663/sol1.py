def dfs(a):

    stack = []
    row = []
    cnt = 0

    stack.append([0, a])

    while stack:

        # if stack:
        now = stack.pop()
        j = now[0] + 1
        if j == n:
            cnt += 1
            break
        else:
            if len(row) == 0:
                row.append(now)
            elif now[0] == row[-1][0] + 1:
                row.append(now)
            else:
                while now[0] < row[-1][0] + 1:
                    row.pop()
                row.append(now)
            # row.append(now[0]+now[1])
            # row.append(now[1]-now[0])

        # else:
        #     break

        # for k in range(a):
        #     if k not in row and k+j not in row and k-j not in row:
        #     # if k not in row:
        #         stack.append([j, k])
        for k in range(a):
            for r in row:
                if k != r[1] and k+j != r[0]+r[1] and k-j != r[1]-r[0]:
                    stack.append([j, k])
                    print(row)
                    print(stack)

        # else:
        #     row.pop()
            # row.pop()
            # row.pop()

    return cnt


n = int(input())

for i in range(n):
    print(dfs(i))

