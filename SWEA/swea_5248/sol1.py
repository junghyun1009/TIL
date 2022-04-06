import sys

sys.stdin = open('input.txt')


def find(a):

    if a == parent[a]:
        return a
    else:
        return find(parent[a])


T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())
    team = list(map(int, input().split()))

    parent = [0] * (N + 1)

    for i in range(1, N + 1):
        parent[i] = i

    for t in range(M):
        pick = team[2 * t]
        picked = team[2 * t + 1]
        parent[find(picked)] = find(pick)

    rlt = []
    for i in range(N+1):
        rlt.append(find(i))

    rlt = set(rlt)

    print(f'#{tc} {len(rlt) - 1}')

