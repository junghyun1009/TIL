N = int(input())
members = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    members.append([a, b])
members.sort(key=lambda x:x[0])

for i in members:
    print(i[0], i[1])