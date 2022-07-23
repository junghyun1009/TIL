T = int(input())

for tc in range(1, T + 1):
    quiz = input()

    circle = 0
    circle_list = []
    score = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O' and i != len(quiz) - 1:
            circle += 1
        elif quiz[i] == 'O' and i == len(quiz) - 1:
            circle += 1
            circle_list.append(circle)
        else:
            circle_list.append(circle)
            circle = 0

    for j in circle_list:
        tmp = 0
        for k in range(1, j + 1):
            tmp += k
        score += tmp

    print(score)