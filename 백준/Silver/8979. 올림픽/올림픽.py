import sys
input = sys.stdin.readline

N, K = map(int, input().split(' '))
medal = [list(map(int, input().split(' '))) for _ in range(N)]

for m in medal:
    country = m.pop(0)
    m.append(country)

medal.sort(reverse=True)

place = [1]
for i in range(1, N):
    # 앞의 국가와 같은 메달 수인 경우
    if medal[i][0:3] == medal[i-1][0:3]:
        place.append(place[i-1])
    # 메달 수가 다른 경우
    else:
        place.append(i+1)

for j in range(N):
    if medal[j][3] == K:
        print(place[j])