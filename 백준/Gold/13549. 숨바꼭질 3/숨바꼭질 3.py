from collections import deque

N, K = map(int, input().split(' '))
q = deque()
visited = [100001] * 100001
q.append([N, 0])

while q:
    now, time = q.popleft()
    
    if now == K:
        print(time)
        break

    # if abs(now*2-K) < abs(now-K):
    if (0 <= now*2 < len(visited)) and (visited[now*2] > time):
        q.append([now*2, time])
        visited[now*2] = time
##            elif now*2 >= len(visited):
##                q.append([now*2, time])
##                visited += [100001] * (now*2+1-len(visited))
##                visited[now*2] = time
            
    if (0 <= now-1 < len(visited)) and (visited[now-1] > time+1):
        q.append([now-1, time+1])
        visited[now-1] = time+1
##        elif now-1 >= len(visited):
##            q.append([now-1, time+1])
##            visited += [100001] * (now-len(visited))
##            visited[now-1] = time+1

    if (0 <= now+1 < len(visited)) and (visited[now+1] > time+1):
        q.append([now+1, time+1])
        visited[now+1] = time+1
##        elif now+1 >= len(visited):
##            q.append([now+1, time+1])
##            visited += [100001] * (now+2-len(visited))
##            visited[now+1] = time+1

