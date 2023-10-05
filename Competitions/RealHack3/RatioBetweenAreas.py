import math

a,b = tuple(map(float,input().split()))
c,d = tuple(map(float,input().split()))
r = float(input())
ang = float(input())

pi = 3.14
base = ((a-c)**2+(b-d)**2)**0.5
triangleArea = 0.5*base*r*math.sin(ang/2)
circleArea = pi*r**2
angRatio = ang/(pi*2)
ratio = (circleArea*angRatio-triangleArea)/(circleArea*(1-angRatio)-triangleArea)

print("%.2f" %min(ratio,1/ratio))