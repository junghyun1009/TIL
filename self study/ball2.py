import math

HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
r = 5.73
ball_list = [[100,63],[1,1],[1,126],[126,126],[253,126],[253,1],[126,1]]
white_ball = ball_list[0]
target_ball = ball_list[1:]

for ball in target_ball:
    min_route = 999999
    for i in HOLES:
        route = math.sqrt((i[0] - ball[0])**2 + (i[1] - ball[1])**2)
        if min_route > route:
            min_route = route
            min_hole = i

    route_x = abs(ball[0] - min_hole[0])
    route_y = abs(ball[1] - min_hole[1])
    route_radian = math.atan(route_y / route_x)
    hit_x = ball[0]
    hit_y = ball[1]
    
    # 구멍이 타겟의 왼쪽 위
    if min_hole[0] <= ball[0] and min_hole[1] >= ball[1]:
        hit_x += 2 * r * math.cos(route_radian)
        hit_y -= 2 * r * math.sin(route_radian)

    # 구멍이 타겟의 오른쪽 위
    elif min_hole[0] >= ball[0] and min_hole[1] >= ball[1]:
        hit_x -= 2 * r * math.cos(route_radian)
        hit_y -= 2 * r * math.sin(route_radian)

    # 구멍이 타겟의 오른쪽 아래
    elif min_hole[0] >= ball[0] and min_hole[1] <= ball[1]:
        hit_x -= 2 * r * math.cos(route_radian)
        hit_y += 2 * r * math.sin(route_radian)

    # 구멍이 타겟의 왼쪽 아래
    elif min_hole[0] <= ball[0] and min_hole[1] <= ball[1]:
        hit_x += 2 * r * math.cos(route_radian)
        hit_y += 2 * r * math.sin(route_radian)

    move_x = abs(hit_x - white_ball[0])
    move_y = abs(hit_y - white_ball[1])
    radian = math.atan(move_y / move_x)
    angle = math.degrees(radian)
    
    # 이동 지점이 흰 공 왼쪽 위
    if hit_x < white_ball[0] and hit_y > white_ball[1]:
        angle = math.degrees(radian) + 270
    # 이동 지점이 흰 공 오른쪽 위
    elif hit_x > white_ball[0] and hit_y > white_ball[1]:
        angle = 90 - math.degrees(radian)
    # 이동 지점이 흰 공 오른쪽 아래
    elif hit_x > white_ball[0] and hit_y < white_ball[1]:
        angle = 90 + math.degrees(radian)
    # 이동 지점이 흰 공 왼쪽 아래
    elif hit_x < white_ball[0] and hit_y < white_ball[1]:
        angle = 270 - math.degrees(radian)

    print(angle)