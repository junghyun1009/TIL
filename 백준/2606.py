# def dfs(x, y):
#     if v[x] == 1:
#         v[y] = 1
#         return True
#     elif v[y] == 1:
#         v[x] = 1
#         return True
#     return False
#
#
# n = int(input())
# m = int(input())
# a = [list(map(int, input().split())) for _ in range(m)]
#
# v = [0] * (n+1)
# v[1] = 1
#
# for i in a:
#     dfs(i[0], i[1])
# # print(v)
# rlt = v.count(1) - 1
# print(rlt)
n = int(input())
m = int(input())
graph = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0] * (n + 1)


def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)

dfs(1)
print(graph)
print(cnt)

