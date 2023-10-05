n = int(input())

def binary_search(arr, val, start, end):
     
    # we need to distinguish whether we
    # should insert before or after the
    # left boundary. imagine [0] is the last
    # step of the binary search and we need
    # to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    # this occurs if we are moving
    # beyond left's boundary meaning
    # the left boundary is the least
    # position to find a number greater than val
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
 
def insertion_sort(n):
    arr = []
    for i in range(n):
        val = int(input())
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i]
        if i==0:
            print(float(arr[0]))    
        elif i%2==0:
            print(float(arr[int(i/2)]))
        else:
            print((arr[int((i+1)/2)]+arr[int((i-1)/2)])/2)
    return arr




# n = int(input())

# readings = []

# for i in range(n):
#     readings.append(int(input()))
#     readings.sort()
#     if i==0:
#         print(float(readings[0]))    
#     elif i%2==0:
#         print(float(readings[int(i/2)]))
#     else:
#         print((readings[int((i+1)/2)]+readings[int((i-1)/2)])/2)