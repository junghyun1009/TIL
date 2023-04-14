from collections import deque

def solution(n, computers):
    global visited, answer
    answer = 0
    visited = [0] * n
    
    def bfs(start, computers):
        global visited, answer
        
        q = deque()
        q.append(start)
        visited[start] = 1
        
        while q:
            cur = q.popleft()
            for idx in range(n):
                if idx != cur and computers[cur][idx] == 1 and visited[idx] == 0:
                    q.append(idx)
                    visited[idx] = 1
        answer += 1    
        return 
    
    for i in range(n):
        if visited[i] == 0:
            bfs(i, computers)
        
    return answer