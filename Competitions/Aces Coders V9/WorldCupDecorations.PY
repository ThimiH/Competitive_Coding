from math import pi, sin  

n,r,c = tuple(map(int,input().split()))

R = r*sin(pi/n)/(1-sin(pi/n))
area = n*pi*R**2+pi*r**2
cost = c*area
print("%.3f" %cost)