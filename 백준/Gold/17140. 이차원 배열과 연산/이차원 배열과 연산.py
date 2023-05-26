r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

target = [r-1, c-1]
time = 0

# 테스트 용 -> 두 줄 지우기
##row_cnt = len(A[0])
##col_cnt = len(A)

while True:
    row_cnt = len(A)
    col_cnt = len(A[0])

    if (0 <= target[0] < row_cnt) and (0 <= target[1] < col_cnt) and (A[target[0]][target[1]] == k):
        break
    elif time >= 100:
        time = -1
        break

    time += 1
    # print(time)
    
    # 행 >= 열
    if row_cnt >= col_cnt:
        max_row = 0
        
        # 각 행마다 숫자 종류 확인
        for row in range(row_cnt):
            order = []
            numbers = list(set(A[row]))
            for num in numbers:
                if num > 0:
                    cnt = 0
                    for a in A[row]:
                        if num == a:
                            cnt += 1
                    order.append([num, cnt])
            order = sorted(order, key = lambda x : (x[1], x[0]))
            
            # 정렬한 배열 합치기
            tmp = order[0]
            for i in range(1, len(order)):
                tmp += order[i]
            A[row] = tmp
            if max_row < len(tmp):
                max_row = len(tmp)

        # 각 행마다 빈칸 0으로 채워주기
        for idx in range(len(A)):
            A[idx] += [0] * (max_row - len(A[idx]))

        # print(A)

    # 행 < 열
    else:
        # 행, 열 자리 바꿔주기
        B = []
        for col in range(len(A[0])):
            row_tmp = []
            for row in range(len(A)):
                row_tmp.append(A[row][col])
            B.append(row_tmp)
        # print(B)

        # A = [arr[:] for arr in B]

        # 연산 똑같이
        max_row = 0
        
        # 각 행마다 숫자 종류 확인
        for row in range(len(B)):
            order = []
            numbers = list(set(B[row]))
            for num in numbers:
                if num > 0:
                    cnt = 0
                    for b in B[row]:
                        if num == b:
                            cnt += 1
                    order.append([num, cnt])
            order = sorted(order, key = lambda x : (x[1], x[0]))
            
            # 정렬한 배열 합치기
            tmp = order[0]
            for i in range(1, len(order)):
                tmp += order[i]
            B[row] = tmp
            if max_row < len(tmp):
                max_row = len(tmp)

        # 각 행마다 빈칸 0으로 채워주기
        for idx in range(len(B)):
            B[idx] += [0] * (max_row - len(B[idx]))

        # 다시 뒤집기
        C = []
        for col in range(len(B[0])):
            row_tmp = []
            for row in range(len(B)):
                row_tmp.append(B[row][col])
            C.append(row_tmp)

        A = [arr[:] for arr in C]
        # print(A)

print(time)
        
        
        
