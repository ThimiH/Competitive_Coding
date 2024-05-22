# 33.33 marks Some wrong, some time fail

import math

def angle_with_x_axis(point1, point2):
    delta_x = point2[0] - point1[0]
    delta_y = point2[1] - point1[1]
    angle_radians = math.atan2(delta_y, delta_x)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

for test in range(int(input())):
    plus = []
    minus = []
    for point in range(int(input())):
        x,y,z = tuple(map(float,input().split()))
        if z == 1:
            plus.append((x,y))
        else:
            minus.append((x,y))
    max_1 = -180.0
    max_2 = 0.0
    min_1 = 180.0
    min_2 = 360.0
    for plus_point in plus:
        for min_point in minus:
            ang_1 = angle_with_x_axis(plus_point,min_point)
            ang_2 = ang_1+360 if ang_1<0 else ang_1
            max_1 = max(ang_1,max_1)
            max_2 = max(ang_2,max_2)
            min_1 = min(ang_1,min_1)
            min_2 = min(ang_2,min_2)
    if max_1-min_1 <= 180 or max_2-min_2 <= 180:
        print('YES')
    else:
        print('NO')