while True:
    A, B, C = map(int, input().split(' '))
    
    if [A, B, C] == [0, 0, 0]:
        break

    maxLength = max(A, B, C)

    if maxLength >= sum([A, B, C]) - maxLength:
        print("Invalid")

    elif A == B and B == C and C == A:
        print("Equilateral")

    elif A == B or B == C or C == A:
        print("Isosceles")

    else:
        print("Scalene")