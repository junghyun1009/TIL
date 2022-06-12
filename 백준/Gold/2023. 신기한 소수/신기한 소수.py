def check(a):
    for i in range(3, int(a**(1/2)), 2):
        if a % i == 0:
            return False
    return True

def dfs(tmp):

    if 1 <= len(tmp) <= N:
        num = int(tmp)
        if check(num) == False:
            return

        elif len(tmp) == N:
            print(tmp)
            return
    
    for i in can:
        if len(tmp) == 0 and i != 1 and i != 9:    
            dfs(tmp + str(i))
        elif len(tmp) != 0 and i % 2 == 1 and i != 5:
            dfs(tmp + str(i))

N = int(input())
can = [1, 2, 3, 5, 7, 9]
dfs('')