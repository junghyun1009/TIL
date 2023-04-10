import sys

H, W, N, M = map(int, input().split(' '))
row = M + 1
col = N + 1

if W % row:
    w = W // row + 1
else:
    w = W // row

if H % col:
    h = H // col + 1
else:
    h = H // col

print(w * h)
