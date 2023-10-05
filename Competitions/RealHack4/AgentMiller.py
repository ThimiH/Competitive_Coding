def power(k,n):
    binnum = bin(n)[2:]
    mod = 10**8+7
    powers = [k]
    for _ in range(len(bin(n))-3):
        powers.append((powers[-1]**2)%mod)

    powers = powers[::-1]

    answer = 1

    for i in range(len(bin(n))-2):
        if int(binnum[i]):
            answer  = (answer*powers[i])%mod
    print(powers)
    return answer

for case in range(int(input())):
    n,l = tuple(map(int,input().split()))
    if l>2:
        firstpart = power(n,l-2)
        ans = (n-n//2)*(n-n//2)
        for i in range(n-n//2):
            ans += n-(2*i+1)
        print((firstpart*ans)%(10**8+7))
    elif l==2:
        ans = (n-n//2)*(n-n//2)
        for i in range(n-n//2):
            ans += n-(2*i+1)
        print(ans)
    else:
        print(n//2)