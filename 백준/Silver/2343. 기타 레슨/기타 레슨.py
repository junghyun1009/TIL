def bsearch(s, e):
    while s <= e:
        mid = (s + e) // 2
        blue = 0
        cnt = 0
        for i in video:
            if blue + i <= mid:
                blue += i
            else:
                # print(mid, i, blue, cnt)
                cnt += 1
                blue = i
        cnt += 1
        # 블루레이 크기 키워야 함
        if cnt > M:
            s = mid + 1
        # 블루레이 크기 줄여야 함
        else:
            candidate.append(mid)
            e = mid - 1

N, M = map(int, input().split())
video = list(map(int, input().split()))
start = max(max(video), int(sum(video) / M))

candidate = []
bsearch(start, sum(video))
# print(candidate)
print(min(candidate))