import sys
input = sys.stdin.readline

N, L = map(int, input().split(' '))
road = [list(map(int, input().split(' '))) for _ in range(N)]

ans = 0

# 가로
for r in range(N):
    row = []
    for c in range(N):
        row.append(road[r][c])

    diff = []
    sign = []
    flag = 0
    for i in range(N-1):
        if -1 <= row[i+1]-row[i] <= 1:
            diff.append(row[i+1]-row[i])
            if row[i+1]-row[i] == -1:
                sign.append('-')
            elif row[i+1]-row[i] == 1:
                sign.append('+')
        else:
            flag = 1
            break

    if flag == 0:            
        # 1. 모두 같은 높이인 경우
        if (diff == [0] * (N-1)):
            # print(row)
            ans += 1
        
        # 2. 낮은 곳(연속 L개 이상)에서 높은 곳으로 가는 경우
        elif ('+' in sign) and ('-' not in sign):
            upper = [0] * (L-1)
            upper.append(1)
            for j in range(N-L):
                if diff[j:j+L] == upper:
                    diff[j:j+L] = ['_'] * L
            if 1 not in diff:
                # print(row)
                ans += 1
                
        # 3. 높은 곳에서 낮은 곳(연속 L개 이상)으로 가는 경우    
        elif ('-' in sign) and ('+' not in sign):
            lower = [0] * (L-1)
            lower.insert(0, -1)
            for j in range(N-L):
                if diff[j:j+L] == lower:
                    diff[j:j+L] = ['_'] * L
            if -1 not in diff:
                # print(row)
                ans += 1

        # 4. 둘 다 있는 경우
        elif ('-' in sign) and ('+' in sign):
            upper = [0] * (L-1)
            upper.append(1)
            lower = [0] * (L-1)
            lower.insert(0, -1)
            for j in range(N-2*L):
                if diff[j:j+2*L] == lower+upper:
                    flag = 2
                    break
            if flag == 0:
                for j in range(N-L):
                    if diff[j:j+L] == upper:
                        diff[j:j+L] = ['_'] * L

                for j in range(N-L):
                    if diff[j:j+L] == lower:
                        diff[j:j+L] = ['_'] * L

                if (1 not in diff) and (-1 not in diff):
                    # print(row)
                    ans += 1
                
# print(ans)
# 세로
for c in range(N):
    col = []
    for r in range(N):
        col.append(road[r][c])

    diff = []
    sign = []
    flag = 0
    for i in range(N-1):
        if -1 <= col[i+1]-col[i] <= 1:
            diff.append(col[i+1]-col[i])
            if col[i+1]-col[i] == -1:
                sign.append('-')
            elif col[i+1]-col[i] == 1:
                sign.append('+')
        else:
            flag = 1
            break

    if flag == 0:            
        # 1. 모두 같은 높이인 경우
        if (diff == [0] * (N-1)):
            # print(col)
            ans += 1
        
        # 2. 낮은 곳(연속 L개 이상)에서 높은 곳으로 가는 경우
        elif ('+' in sign) and ('-' not in sign):
            upper = [0] * (L-1)
            upper.append(1)
            for j in range(N-L):
                if diff[j:j+L] == upper:
                    diff[j:j+L] = ['_'] * L
            if 1 not in diff:
                # print(col)
                ans += 1
                
        # 3. 높은 곳에서 낮은 곳(연속 L개 이상)으로 가는 경우    
        elif ('-' in sign) and ('+' not in sign):
            lower = [0] * (L-1)
            lower.insert(0, -1)
            for j in range(N-L):
                if diff[j:j+L] == lower:
                    diff[j:j+L] = ['_'] * L
            if -1 not in diff:
                # print(col)
                ans += 1

        # 4. 둘 다 있는 경우
        elif ('-' in sign) and ('+' in sign):
            upper = [0] * (L-1)
            upper.append(1)
            lower = [0] * (L-1)
            lower.insert(0, -1)
            for j in range(N-2*L):
                if diff[j:j+2*L] == lower+upper:
                    flag = 2
                    break
            if flag == 0:
                for j in range(N-L):
                    if diff[j:j+L] == upper:
                        diff[j:j+L] = ['_'] * L

                for j in range(N-L):
                    if diff[j:j+L] == lower:
                        diff[j:j+L] = ['_'] * L
                        
                if (1 not in diff) and (-1 not in diff):
                    # print(col)
                    ans += 1
                
print(ans)
