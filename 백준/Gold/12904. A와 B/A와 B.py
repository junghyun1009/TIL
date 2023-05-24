S = input()
T = input()
answer = 0

while True:
    if len(T) == len(S):
        if T == S:
            answer = 1
        break
            
    if T[-1] == 'A':
        T = T[:-1]
    else:
        T = T[:-1][::-1]

print(answer)