def fib(Nlst):
    Nlstc = 0
    Ndct = {}
    fn_= 0
    fn = 1
    for i in range(2,Nlst[-1]+1):
        f_ = fn_
        fn_ = fn
        fn = (f_+fn_)%10**9
        if Nlst[Nlstc] == i:
            Ndct[Nlst[Nlstc]]=fn
            Nlstc+=1
    return Ndct
        
T = int(input())

if 0<T<=10:
    Nlst = []
    for val in range(T):
        Nlst.append(int(input()))
    Nlststd = Nlst[:]
    Nlststd.sort()

    if 40<=Nlststd[0] and Nlststd[-1]<=10**18:
        Nlstftd = []
        for num in Nlststd:
            if num not in Nlstftd:
                Nlstftd.append(num)
        Ndct = fib(Nlstftd)

        for n in Nlst:
            print(Ndct[n])