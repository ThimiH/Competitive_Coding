t=int(input())
for x in range(t):
 n=int(input())
 c='The IEEEXtreme 16.0 competition starts in days.'
 if n==22:print('Today is the day!')
 elif n==21:print(c[:3]+c[19:39]+'tomorrow.')
 else:print(c[:42]+str(22-n)+c[41:])