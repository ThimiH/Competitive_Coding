#
# Complete the 'mandragora' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY H as parameter.
#

def mandragora(H):
    H.sort()
    health = 1
    health_point_sum = 0
    for health_point in H:
        health_point_sum += health_point
    xp_point = health_point_sum
    for health_point in H:
        health += 1
        health_point_sum -= health_point
        if xp_point <= health * health_point_sum:
            xp_point = health * health_point_sum
        else:
            break
    return xp_point