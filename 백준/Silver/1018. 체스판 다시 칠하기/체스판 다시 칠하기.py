N, M = map(int, input().split())
chess = [input() for _ in range(N)]
check = []
type_a = 'WBWBWBWB'
type_b = 'BWBWBWBW'

for x in range(N - 7):
    for c in range(M - 7):
        # mini = []
        one = 0
        two = 0
        for r in range(x, x + 8):
            tmp = chess[r][c:c+8]
            # mini.append(tmp)
            if r % 2:
                for i in range(8):
                    if i % 2 == 0 and tmp[i] == 'B':
                        one += 1
                    elif i % 2 == 1 and tmp[i] == 'W':
                        one += 1
                    elif i % 2 == 0 and tmp[i] == 'W':
                        two += 1
                    elif i % 2 == 1 and tmp[i] == 'B':
                        two += 1
            else:
                for i in range(8):
                    if i % 2 == 0 and tmp[i] == 'W':
                        one += 1
                    elif i % 2 == 1 and tmp[i] == 'B':
                        one += 1
                    elif i % 2 == 0 and tmp[i] == 'B':
                        two += 1
                    elif i % 2 == 1 and tmp[i] == 'W':
                        two += 1
        # pprint(mini)
        check.append(min(one, two))

print(min(check))