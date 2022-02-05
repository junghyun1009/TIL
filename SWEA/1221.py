t = int(input())
for tc in range(1, t+1):
    n = input()
    a = list(map(input().split()))
#a = ['TWO', 'NIN', 'TWO','EGT', 'TWO', 'SVN', 'FIV', 'SIX', 'FOR', 'ONE', 'ZRO', 'THR']

# order = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
# tmp = []
# for index, number in enumerate(order):

    a_match = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    b_match = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}
    tmp = []
    tmp_2 = []

    for num in a:
        tmp.append(a_match.get(num))
    tmp = sorted(tmp)

    print(f'#{tc}')
    for number in tmp:
        print(b_match.get(number), end=' ')

  