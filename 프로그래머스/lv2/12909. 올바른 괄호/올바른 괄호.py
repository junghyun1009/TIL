from collections import deque

def solution(s):
    answer = True
    A = deque(s)
    queue = []
    while A:
        if A[0] == '(':
            A.popleft()
            queue.append('(')
        else:
            if len(queue):
                A.popleft()
                queue.pop(-1)
            else:
                return False
    if len(queue) != 0:
        answer = False

    return answer