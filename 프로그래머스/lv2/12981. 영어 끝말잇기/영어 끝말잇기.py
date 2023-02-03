def solution(n, words):
    answer = [0, 0]
    last = ''
    stack = []
    
    for idx, word in enumerate(words):
        # 맨 첫번째
        if last == '':
            last = word[-1]
            stack.append(word)
        # 끝 글자가 다른 경우
        elif last != word[0]:
            answer[0] = idx % n + 1
            answer[1] = idx // n + 1
            break
        # 끝 글자가 같은 경우
        else:
            # 이미 나온 단어인 경우
            if word in stack:
                answer[0] = idx % n + 1
                answer[1] = idx // n + 1
                break
            # 아직 안 나온 단어인 경우
            else:
                stack.append(word)
                last = word[-1]

    return answer