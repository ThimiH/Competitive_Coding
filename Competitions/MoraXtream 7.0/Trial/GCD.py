from ast import Num


lt = [6,8,16]

def GCD(lst):
    lst.sort()
    min = lst[0]
    while min > 1 :
        count = 0
        for item in lst:
            if item % min != 0:
                min -= 1
                break
            else:
                count += 1
        if count == len(lst):
            return min
    return 1
             

print(GCD(lt))