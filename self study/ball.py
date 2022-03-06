import math

HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
r = 5.73
white_ball = [100, 63]
target_ball = [200, 40]

min_route = 99999999

for i in HOLES:
    route = math.sqrt((i[0]-target_ball[0])**2 + (i[1]-target_ball[1])**2)
    if min_route > route:
        min_route = route
        min_HOLE = i

target_width = abs(target_ball[0] - min_HOLE[0])
target_height = abs(target_ball[1] - min_HOLE[1])
target_radian = math.atan(target_height/target_width)

hit_point_x = target_ball[0]
hit_point_y = target_ball[1]

# 구멍이 왼쪽 위에 있을 때
if target_ball[0] > min_HOLE[0] and target_ball[1] > min_HOLE[1]:
    hit_point_x += 2 * r * math.cos(target_radian)
    hit_point_y += 2 * r * math.sin(target_radian)

# 구멍이 왼쪽 아래에 있을 때
elif target_ball[0] > min_HOLE[0] and target_ball[1] < min_HOLE[1]:
    hit_point_x += 2 * r * math.cos(target_radian)
    hit_point_y -= 2 * r * math.sin(target_radian)

# 구멍이 오른쪽 위에 있을 때
elif target_ball[0] < min_HOLE[0] and target_ball[1] > min_HOLE[1]:
    hit_point_x -= 2 * r * math.cos(target_radian)
    hit_point_y += 2 * r * math.sin(target_radian)

# 구멍이 오른쪽 아래에 있을 때
elif target_ball[0] < min_HOLE[0] and target_ball[1] < min_HOLE[1]:
    hit_point_x -= 2 * r * math.cos(target_radian)
    hit_point_y -= 2 * r * math.sin(target_radian)


move_x = abs(hit_point_x - white_ball[0])
move_y = abs(hit_point_y - white_ball[1])

hit_radian = math.atan(move_y / move_x)
angle = hit_radian * (180 / math.pi)

# 타격지점이 흰공의 왼쪽 위에 있을 때 (2사분면)
if hit_point_x < white_ball[0] and hit_point_y < white_ball[1]:
    hit_radian = math.atan(move_y / move_x)
    angle = 90 + hit_radian * (180 / math.pi)

# 타격지점이 흰공의 왼쪽 아래에 있을 때 (3사분면)
elif hit_point_x < white_ball[0] and hit_point_y > white_ball[1]:
    hit_radian = math.atan(move_y / move_x)
    angle = 90 - hit_radian * (180 / math.pi)

# 타격지점이 흰공의 오른쪽 위에 있을 때 (1사분면)
elif hit_point_x > white_ball[0] and hit_point_y < white_ball[1]:
    hit_radian = math.atan(move_y / move_x)
    angle = 270 - hit_radian * (180 / math.pi)

# 타격지점이 흰공의 오른쪽 아래에 있을 때 (4사분면)
elif hit_point_x > white_ball[0] and hit_point_y > white_ball[1]:
    hit_radian = math.atan(move_y / move_x)
    angle = 270 + hit_radian * (180 / math.pi)

print(min_HOLE)
# print(min_route)
# print(target_radian)
print(hit_point_x, hit_point_y)
# print(move_x, move_y)
# print(hit_radian)
print(angle)