word = input()

# 소문자를 대문자로 변환해서 갯수 세기
cnt = []
word = word.upper()
nooverlap = list(set(word))

for i in nooverlap:
    cnt_alph = word.count(i)
    if [cnt_alph, i] not in cnt:
        cnt.append([cnt_alph, i])

max_cnt = max(cnt)[0]
max_alph = max(cnt)[1]

ismany = 0
for j in cnt:
    if j[0] == max_cnt:
        ismany += 1
    if ismany == 2:
        break

if ismany > 1:
    print('?')
else:
    print(max_alph)