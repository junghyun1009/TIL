a = []
for num in range(9):
    a.append(int(input()))

a = sorted(a)

liars = sum(a) - 100

for i in a:
    if liars - i in a:
        a.remove(i)
        a.remove(liars-i)
        break

for j in a:
    print(j)