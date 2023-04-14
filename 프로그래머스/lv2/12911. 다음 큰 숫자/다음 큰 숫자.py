def solution(n):
    answer = 0
    cur = str(bin(n))
    cnt = 0
    for c in cur:
        if c == '1':
            cnt += 1
    next_bigger = n + 1
    while True:
        next_binary = str(bin(next_bigger))
        check = 0
        for n in next_binary:
            if n == '1':
                check += 1
        if check == cnt:
            answer = next_bigger
            break
        else:
            next_bigger += 1
        
    return answer