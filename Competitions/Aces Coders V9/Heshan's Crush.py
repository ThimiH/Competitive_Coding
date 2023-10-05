u,v,l = tuple(map(float,input().split()))
print("%.4f" %(((3*v+u)*l)/((v+3*u)*v)))

# x = 2*l/((v/u)+3)
# ans = x/u+(l-x)/v
# ans = str(round(ans,4))
# ans = ans.split('.')
# while len(ans[1])<=5:
#     ans[1]+='0'
# print(*ans, sep='.')