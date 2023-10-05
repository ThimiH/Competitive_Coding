# O(nlogn) approach

# Correct this
n = int(input()) 

sequence = []

for num in range(n):
    sequence.append(int(input()) )

length = len(sequence)

subseq = [sequence[0]]

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

def current_longest_subsequence(element):
    global subseq
    if subseq[-1]<=element:
        subseq.append(element)
    else:
        index = binary_search(subseq,element)
        subseq[index] = element

for element in sequence[1:]:
    current_longest_subsequence(element)

print(len(subseq))

'''
O(n^2) approach

n = int(input()) 

sequence = []

for num in range(n):
    sequence.append(int(input()) )

length = len(sequence)
sublen = []
maxlen = 0


def longest_increasing_subsequence(sequence,ind):
    global sublen
    global maxlen
    sublen.append(1)
    for i in range(ind):
        if sequence[ind]>sequence[i]:
            if sublen[ind]<=sublen[i]:
                sublen[ind] = sublen[i]+1
                if sublen[ind]>maxlen:
                    maxlen = sublen[ind]
                    break
    return None

for ind in range(length):
    longest_increasing_subsequence(sequence,ind)

print(maxlen)
'''