N, G = input().split(' ')
N = int(N)
player = [input() for _ in range(N)]

# 1. 중복 제거
player = list(set(player))

cnt = 0
if G == 'Y':
    cnt = len(player)
elif G == 'F':
    cnt = len(player) // 2
elif G == 'O':
    cnt = len(player) // 3

print(cnt)