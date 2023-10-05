#binary search to find lowest values index in list higher than or equal to val 
def binsearchup(lst,val):
    length = len(lst)
    a,b = 0,length
    while a+1!=b:
        i = (a+b)//2
        if lst[i]<=val:
            a = i
        else:
            b = i
    return b

def binary_search(sequence,value):
    #Returns the index of lowest number in distinct value sequence that is bigger than the value.
    length = len(sequence)
    if length == 0:
        return None
    elif length == 1:
        return 0
    else:
        lower_bound = 0
        upper_bound = length-1
        while lower_bound+1<upper_bound:
            index = (lower_bound + upper_bound)//2
            if sequence[index]>value:
                upper_bound = index
            else:
                lower_bound = index
        return upper_bound
    
sequence = [1,3,4,6,9,34,56,57,101,211,222,245,555,789,2544,4565]
value = 4580


print(sequence[binary_search(sequence,value)])