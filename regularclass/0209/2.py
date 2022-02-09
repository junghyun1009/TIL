a = 112244 # 123444 333444 123567 111123 112233

b = ','.join(str(a)) # a를 문자열로 바꾸고 사이에 , 추가해주기
c = list(map(int, b.split(','))) # a의 각각의 숫자를 list로 받아오기

c = sorted(c)

ca = c[0:3] # 앞에 3개 슬라이싱
cb = c[3:6] # 뒤에 3개 슬라이싱


if ca[0]==ca[1]==ca[2] or (ca[2]==ca[1]+1 and ca[1]==ca[0]+1): # 3개의 원소가 다 똑같거나 연속하는 숫자인 경우 1 저장
    rlt_a = 1
else: # 아니라면 0 저장
    rlt_a = 0


if cb[0]==cb[1]==cb[2] or (cb[2]==cb[1]+1 and cb[1]==cb[0]+1): # 3개의 원소가 다 똑같거나 연속하는 숫자인 경우 1 저장
    rlt_b = 1
else: # 아니라면 0 저장
    rlt_b = 0


for number in c:
    if c.count(number) == 2:
        tmp = number
        c = c[2:]
        if tmp == number-1:
            continue

if len(c) == 0:
    rlt_a = 1
    rlt_b = 1

print(rlt_a and rlt_b) # ca와 cb의 결과 병합

