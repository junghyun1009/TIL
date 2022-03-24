def dfs(start):

    if len(team) == n//2:
        rlt = team[:]
        team_set.append(rlt)
        # print(team_set)
        return

    for i in range(start, n):
        if i not in team:
            team.append(i)
            dfs(i+1)
            team.pop()


def dfs2(arr):

    if len(match) == 2:
        rlt = match[:]
        num_set.append(rlt)
        # print(team_set)
        return

    for i in arr:
        if i not in match:
            match.append(i)
            dfs2(arr)
            match.pop()


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
team = [0]
team_set = []
score = []
dfs(0)
# print(team_set)

for i in team_set:
    a = i
    b = []
    for j in range(n):
        if j not in a:
            b.append(j)

    match = []
    num_set = []
    a_score = 0
    dfs2(a)
    # print(num_set)
    for k in num_set:
        a_score += s[k[0]][k[1]]

    match = []
    num_set = []
    b_score = 0
    dfs2(b)
    # print(num_set)
    for l in num_set:
        b_score += s[l[0]][l[1]]

    score.append(abs(a_score - b_score))

print(min(score))