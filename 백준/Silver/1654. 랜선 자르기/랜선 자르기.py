N, K = map(int, input().split())
line = [int(input()) for _ in range(N)]

end = int(sum(line) / K)
candidate = []

def bsearch(s, e):
    while s <= e:
        mid = (s + e) // 2
        # print(s, e, mid)
        cnt = 0
        for i in line:
            cnt += int(i / mid)
        # print(cnt)
        # 조각이 더 많이 나오면 더 큰 조각으로 자르기
        if cnt == K:
            candidate.append(mid)
            s = mid + 1
        # 조각이 더 적게 나오면 더 작은 조각으로 자르기
        elif cnt < K:
            e = mid - 1
        else:
            candidate.append(mid)
            s = mid + 1

bsearch(1, end)
# print(candidate)
print(max(candidate))