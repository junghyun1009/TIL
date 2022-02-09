a = [7, 4, 2, 0, 0, 6, 0, 7, 0]
fall = []

# 각각의 박스에 대한 낙차 모두 구하기

# a에 있는 한줄의 박스에 대해
for row in range(len(a)):

    # 각각의 박스를 1번부터 번호를 매기고 
    for box in range(1,a[row]+1):

        # 세로열에 대해서 같은 번호를 가진 박스 수 세기
        # 단, 해당 줄의 아랫줄부터 확인해야 함
        cnt = 0
        for check in range(row,len(a)):
            if a[check] >= box:
                cnt += 1
        
        # 각각의 박스의 낙차를 계산하여 리스트에 추가
        # (방 길이)-(인덱스)-(해당 열부터 계산한 같은 번호의 박스 수)
        fall.append(len(a)-row-cnt)

print(max(fall))