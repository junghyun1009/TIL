def solution(n):
    answer = 1
    start = 1
    
    while True:
        if start > n//2:
            break
        cnt = 0
        for i in range(start, n+1):
            cnt += i
            if cnt == n:
                answer += 1
                break
            elif cnt > n:
                break
        start += 1
        
    return answer