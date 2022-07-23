N = int(input())

command = []
for _ in range(N):
    command.append(input())

queue = []

for i in command:
    if i[0:4] == 'push':
        queue.append(int(i[5:]))
    elif i == 'pop':
        if len(queue):
            a = queue.pop(0)
            print(a)
        else:
            print(-1)
    elif i == 'size':
        print(len(queue))
    elif i == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif i == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    else:
        if len(queue):
            print(queue[-1])
        else:
            print(-1)