def solution(s):
    answer = ''
    word = list(s.split(' '))
    # 1. 단어의 첫번째가 숫자라면
    for w in word:
        for idx in range(len(w)):
            if (idx == 0) and (ord(w[idx]) < 65):
                answer += w[idx]
            elif (idx == 0) and (97 <= ord(w[idx])):
                answer += w[idx].upper()
            elif (idx != 0) and (97 <= ord(w[idx])):
                answer += w[idx]
            elif (idx != 0) and (ord(w[idx]) < 97):
                answer += w[idx].lower()
            else:
                answer += w[idx]
        if w != word[-1]:
            answer += ' '
        
    return answer