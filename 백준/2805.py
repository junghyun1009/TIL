import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)

while (start <= end):
    tot = 0
    mid = (start + end) // 2

    for i in tree:

        if i > mid:
            tot += i - mid

    if tot < m:
        end = mid - 1
    else:
        rlt = mid
        start = mid + 1

print(rlt)
