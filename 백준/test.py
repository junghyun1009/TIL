a = [[2, 3, 1, 6, 5, 4], [3, 1, 2, 4, 6, 5], [5, 6, 4, 1, 3, 2], [1, 3, 6, 2, 4, 5], [4, 1, 6, 5, 2, 3]]
tmp = []
max_sum = []
for dice in a:
    tmp.append([[dice[0], dice[5]], [dice[1], dice[3]], [dice[2], dice[4]]])

for first in tmp[0]:
    for i in range(0, 2):
        bottom = first[i]
        first.remove(bottom)
        top = first[0]
        first.insert(0, bottom)
        max_num = max(list(set(a[0])-set(first)))
        
        print(max_num)