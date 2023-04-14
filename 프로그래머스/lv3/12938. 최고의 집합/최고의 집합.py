def solution(n, s):
    answer = [-1]
    if n <= s:
        q = s // n
        r = s - q * n
        answer = [q] * (n-r) + [q+1] * r
    
    return answer