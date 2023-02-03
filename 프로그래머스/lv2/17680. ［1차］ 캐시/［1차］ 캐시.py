from collections import deque

def solution(cacheSize, cities):
    answer = 0
    stack = deque([''] * cacheSize)
    
    for city in cities:
        city = city.lower()
        if stack:
            # 스택 안에 있으면
            if city in stack:
                answer += 1
                stack.remove(city)
                stack.append(city)
            # 스택 안에 없으면
            else:
                answer += 5
                stack.popleft()
                stack.append(city)
        else:
            answer += 5
    
    return answer