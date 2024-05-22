def base10_to_base_n(number, base,i):
    if number == 0:
        return [0]*i
    
    result = []
    while number > 0:
        remainder = number % base
        result = [remainder] + result
        number = number // base
    while len(result)<i:
        result = [0]+result
    return result

for i in range(int(input())):
    b,x = tuple(map(int,input().split()))
    x+=1

    if b == 1:
        print('a')

    else:

        digits = [b]
        while digits[-1]<x:
            digits.append(digits[-1]*b)

        if x == 1:
            print('a')
        else:
            for i,num in enumerate(digits):
                if x > num*(i+1):
                    x -= num*(i+1)
                else:
                    number = (x-1)//(i+1)
                    x = (x-1)%(i+1)
                    break
            
            base_b_number = base10_to_base_n(number,b,i+1)
            print(chr(ord('a')+base_b_number[x]))