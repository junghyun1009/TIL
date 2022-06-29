import sys
input = sys.stdin.readline

def under_search(s, e):
    global pivot

    while s <= e:
        mid = int((s + e) / 2)

        # 암석 통과
        if under[mid] > pivot:
            s = mid + 1
        elif under[mid] < pivot:
            e = mid - 1
        else:
            s = mid + 1
    return e

def upper_search(s, e):
    global pivot

    while s <= e:
        mid = (s + e) // 2

        if upper[mid] > H - pivot + 1:
            s = mid + 1
        elif upper[mid] < H - pivot + 1:
            e = mid - 1
        else:
            s = mid + 1
    return e
                    

N, H = map(int, input().split())
rock = list(int(input()) for _ in range(N))
upper = []
under = []

for i in range(N):
    if i % 2 == 0:
        under.append(rock[i])
        # check.append(rock[i] + 1)
    else:
        upper.append(rock[i])
        # check.append(H - rock[i])

upper.sort(reverse=True)
under.sort(reverse=True)
# check = list(set(check))
# print(check)
# print(under)
# print(upper)

min_rlt = 999999999999

for j in range(1, H + 1):
    pivot = j
    rlt = under_search(0, N//2-1) + upper_search(0, N//2-1) + 2
    if rlt < min_rlt:
        min_rlt = rlt
        cnt = 1
    elif rlt == min_rlt:
        cnt += 1

print(min_rlt, cnt)