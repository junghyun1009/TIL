w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 오위 왼위 왼아 왼위
dx = [1, -1, -1, -1]
dy = [1, 1, -1, 1]
d = 0
x = p
y = q
cnt = 0

while True:

    if cnt == t:
        break

    if 0 <= x+dx[d] <= w and 0 <= y+dy[d] <= h:
        x = x + dx[d]
        y = y + dy[d]
        cnt += 1

    else:
        d = (d+1) % 4


print(x, y)