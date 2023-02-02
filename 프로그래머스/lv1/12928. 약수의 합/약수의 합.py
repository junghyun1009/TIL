def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            if i < n // i:
                answer += i
                answer += n // i
            elif i <= n // i:
                answer += i
            else:
                break
        if i > n / i:
            break
    return answer