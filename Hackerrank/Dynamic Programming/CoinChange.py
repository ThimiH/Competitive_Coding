#DP: Coin Change

#Tuple input
n,m = tuple(map(int,input().split()))

#List input
coinlst = list(map(int,input().split()))

answers = [0 for i in range(n+1)]
answers[0] = 1

for coin in coinlst:
    for ind in range(coin,n+1):
        answers[ind] += answers[ind-coin]

print(answers[-1])