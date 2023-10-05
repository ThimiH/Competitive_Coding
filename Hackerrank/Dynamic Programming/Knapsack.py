def knapsack(inplst,k):
    reachable_numbers = [False for number in range(k+1)]
    for number in inplst:
        true_lst = [0]
        for integer in range(k+1):
            if reachable_numbers[integer]:
                true_lst.append(integer)
        for value in true_lst:
            multiple = number+value
            while multiple < k:
                reachable_numbers[multiple] = True
                multiple += number
            if multiple == k:
                return k
    for value in range(k,0,-1):
        if reachable_numbers[value]:
            return value
    return 0



#Test cases
t = int(input()) 

for test_case in range(t):
    #Tuple input
    n,k = tuple(map(int,input().split()))
    #Remove duplicates
    inplst = list(set(map(int,input().split())))
    inplst.sort()
    print(knapsack(inplst,k))
