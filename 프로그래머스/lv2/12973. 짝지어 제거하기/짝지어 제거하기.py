from collections import deque

def solution(s):
    answer = 1
    string = deque(s)
    first = string.popleft()
    stack = [first]
    
    while string:
        comp = string.popleft()
        if stack:  
            if stack[-1] == comp:
                stack.pop()
            else:
                stack.append(comp)
        else:
            stack.append(comp) 
    
    if stack:
        answer = 0
        
    return answer