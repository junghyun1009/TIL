# 인덱스 수열 만들기(6P2)
def dfs(tmp, n):
    global max_rlt, min_rlt
    
    if tmp == N:
        if max_rlt < n:
            max_rlt = n
        if min_rlt > n:
            min_rlt = n
        return
    
            
    if cal[0] > 0:
        cal[0] -= 1
        dfs(tmp + 1, n + num[tmp])
        cal[0] += 1
        
    if cal[1] > 0:
        cal[1] -= 1
        dfs(tmp + 1, n - num[tmp])
        cal[1] += 1
        
    if cal[2] > 0:
        cal[2] -= 1
        dfs(tmp + 1, n * num[tmp])
        cal[2] += 1
        
    if cal[3] > 0:
        cal[3] -= 1
        dfs(tmp + 1, int(n / num[tmp]))
        cal[3] += 1

    
    
N = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))

# print(num)
# print(cal)

max_rlt = -999999999999999
min_rlt = 99999999999999
dfs(1, num[0])
# print(rlt)

print(max_rlt)
print(min_rlt)