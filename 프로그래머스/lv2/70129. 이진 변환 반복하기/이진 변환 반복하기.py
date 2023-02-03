def solution(s):
    answer = []
    count = 0
    zero = 0
    while True:
        if s == '1':
            answer = [count, zero]
            break
        org = len(s)
        removed = s.replace('0', '')
        zero += org - len(removed)
        s = bin(len(removed)).replace('0b', '')
        count += 1
    return answer