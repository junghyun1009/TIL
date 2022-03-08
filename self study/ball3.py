import math
# balls = [[흰공의 x좌표, 흰공의 y좌표], [1번 목적구의 x좌표, 1번 목적구의 y좌표]...]
# whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
whiteBall_x = gameData.balls[0][0]
whiteBall_y = gameData.balls[0][1]

# targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
for k in range(1, len(gameData.balls)):
    targetBall_x = gameData.balls[k][0]
    targetBall_y = gameData.balls[k][1]

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    width = abs(targetBall_x - whiteBall_x)
    height = abs(targetBall_y - whiteBall_y)

    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과

    radian = math.atan(width / height)
    angle = 180 / math.pi * radian

    # 목적구가 흰 공을 중심으로 2사분면에 위치했을 때 각도를 재계산
    if whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90

    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    elif whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180

    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width ** 2 + height ** 2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.45
