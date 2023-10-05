arr = list(map(int,input().split()))
b,t = tuple(map(int,input().split()))

def CountSort(arr,bottom,top):
    count = [[i,0] for i in range(bottom,top+1)]
    for num in arr:
        count[num-bottom][1] += 1
    stdarr = []
    for item in count:
        for p in range(item[1]):
            stdarr.append(item[0])
    return stdarr

print(CountSort(arr,b,t))