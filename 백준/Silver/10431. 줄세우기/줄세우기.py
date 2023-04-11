import sys
from collections import deque

P = int(input())
for tc in range(1, P+1):
    T = list(map(int, input().split(' ')))
    # 정렬 안 된 학생 줄
    q = deque()
    for t in range(1, 21):
        q.append(T[t])
    # 정렬된 학생 줄
    correct = []
    first = q.popleft()
    correct.append(first)
    cnt = 0
    while q:
        current = q.popleft()
        # print(current, q)
        for c in range(len(correct)):
            if (current > correct[c]) and (c == len(correct)-1):
                correct.append(current)
                # print(correct)
##            elif (current > correct[c]) and (c != len(correct)-1):
##                continue
            elif (current < correct[c]):
                correct.insert(c, current)
                # print(correct)
                for s in range(c+1, len(correct)):
                    cnt += 1
                break
    print(tc, cnt)