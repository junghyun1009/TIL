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

        # tmp = tmp[1:]
        # bottom = top
        # for j in range(0, 3):
        #     if bottom in tmp[0][j]:
def findmax(bottom, dice_num):
    for i in dice_num:
        if bottom in i:
            top = int(set(i)-set(bottom))
            dice_num.remove(i)
            max_num = max(set(dice_num)-{bottom, top})
