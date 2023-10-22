for _ in range(int(input())):
    n = bin(int(input()))[2:][::-1]
    k = n.index('1')+1
    k += n[k:].count('1')
    print('Richard' if k%2==1 else 'Louise')
