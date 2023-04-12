N = int(input())
cookie = [list(input()) for _ in range(N)]
flag = 0

for r in range(N):
    for c in range(N):
        if cookie[r][c] == '*':
            head = [r, c]
            flag = 1
            break
    if flag == 1:
        break

heart = [r+1, c]

left_arm = 0
right_arm = 0
for a in range(heart[1]):
    if cookie[heart[0]][a] == '*':
        left_arm += 1
for b in range(heart[1]+1, N):
    if cookie[heart[0]][b] == '*':
        right_arm += 1

waist = 0
for r in range(heart[0]+1, N):
    if cookie[r][heart[1]] == '*':
        waist += 1
        last = [r, heart[1]]

left_leg = 0
right_leg = 0

for i in range(last[0]+1, N):
    if cookie[i][last[1]-1] == '*':
        left_leg += 1
for j in range(heart[0]+1, N):
    if cookie[j][last[1]+1] == '*':
        right_leg += 1

print(heart[0]+1, heart[1]+1)
print(left_arm, right_arm, waist, left_leg, right_leg)
