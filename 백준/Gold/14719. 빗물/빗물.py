H, W = map(int, input().split())
block = list(map(int, input().split()))

rain = [[1] * W for _ in range(H)]
answer = 0

for w in range(W):
    for r in range(H-block[w]):
        rain[r][w] = 0

for h in range(H):
    tmp = 0
    flag = 0
    for w in range(W):
        # 시작하는 1일 경우 -> 시작 표시
        if rain[h][w] == 1 and flag == 0:
            flag = 1
        # 앞에 1이 있고 0이 나온 경우
        elif rain[h][w] == 0 and flag == 1:
            tmp += 1
        # 끝나는 1일 경우
        elif rain[h][w] == 1 and flag == 1:
            answer += tmp
            tmp = 0

print(answer)
