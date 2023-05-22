N, K = map(int, input().split())
A = list(map(int, input().split()))
robot = [0] * len(A)
robot_cnt = 0
level = 0

while True:
    
    if robot[N-1]:
        robot[N-1] = 0
        robot_cnt -= 1
        for r in range(len(robot)):
            if robot[r] > 0:
                robot[r] -= 1

    # 1. 벨트, 로봇 회전
    last_belt = A.pop()
    last_robot = robot.pop()
    A.insert(0, last_belt)
    robot.insert(0, last_robot)

    # print(A)
    # print(robot)

    i = 1
    while True:
        if i > robot_cnt:
            break

        cur = robot.index(i)

        # 마지막 칸인 경우
        if cur == N-1:
            robot[cur] = 0
            robot_cnt -= 1
            for r in range(len(robot)):
                if robot[r] > i:
                    robot[r] -= 1
            i = 1
            continue
            
        # 다음칸으로 옮길 수 있는 경우
        elif robot[cur+1] == 0 and A[cur+1] >= 1:
            robot[cur+1] = i
            robot[cur] = 0
            A[cur+1] -= 1

        i += 1

##        # 다음칸이 마지막 칸인 경우
##        elif robot[cur+1] == 0 and A[cur+1] >= 1 and (cur+1) == (2*N-1):
##            robot[cur+1] = 0
##            robot[cur] = 0
##            A[cur+1] -= 1
##            robot_cnt -= 1
##            for r in range(len(robot)):
##                if robot[r] > i:
##                    robot[r] -= 1

    if A[0]:
        robot[0] = robot_cnt + 1
        robot_cnt += 1
        A[0] -= 1

    level += 1

    # print(level)
    # print(A)
    # print(robot)
    # print('--------------------')

    zero_cnt = 0
    for a in A:
        if a == 0:
            zero_cnt += 1

    if zero_cnt >= K:
        print(level)
        break
            
