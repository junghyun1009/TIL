a = [
[1,3,3,6,7],
[8,13,9,12,8],
[4,16,11,12,6],
[2,4,1,23,2],
[9,13,4,7,3]]

rlt = []

for i in range(len(a)-1):
    tmp = []
    for j in range(len(a[0])-1):
        tmp.append(a[i][j:j+2])
        break
print(tmp)