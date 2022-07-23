sentence = input()

space = 0

for i in sentence:
    if i == ' ':
        space += 1
        
# 맨 앞과 맨 뒤가 공백인 경우
if sentence[0] == ' ' and sentence[-1] == ' ':
    print(space - 1)
# 맨 앞이 공백인 경우
elif sentence[0] == ' ' and sentence[-1] != ' ':
    print(space)
# 맨 뒤가 공백인 경우
elif sentence[0] != ' ' and sentence[-1] == ' ':
    print(space)
# 맨 앞과 뒤에 공백이 없는 경우
else:
    print(space + 1)