def findSum(number,upperbound):
    value = upperbound // number
    return number*(value*(value+1))//2

t = int(input())

for teatcase in range(t):
    n = int(input())-1
    print(findSum(3,n)+findSum(5,n)-findSum(15,n))