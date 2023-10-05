from math import sin,cos,radians

r,L,h_1,ang_1,h_2,ang_2 = tuple(map(float,input().split()))

if ang_1>ang_2:
    if ang_1-ang_2<180:
        ang_1 -= ang_2
        ang_2 = 0
    else:
        ang_2 += (360-ang_1)
        ang_1 = 0
else:
    if ang_2-ang_1<180:
        ang_2 -= ang_1
        ang_1 = 0
    else:
        ang_1 += (360-ang_2)
        ang_2 = 0

R = (L**2+r**2)**0.5
ang_ratio = r/R
ang_1*=ang_ratio
ang_2*=ang_ratio

d_1 = R*(1-h_1/L)
d_2 = R*(1-h_2/L)

x_1 = d_1*cos(radians(ang_1))
y_1 = d_1*sin(radians(ang_1))
x_2 = d_2*cos(radians(ang_2))
y_2 = d_2*sin(radians(ang_2))

dist = ((x_1-x_2)**2+(y_1-y_2)**2)**0.5

print("%.4f" %dist)

