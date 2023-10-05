T = int(input())

for i in range(T):
    word,n = tuple(input().split())
    n = int(n)
    count=1
    l = len(word)
    for i in range(l):
        count*=(len(set(word[i:min(i+n+1,l+1)])))
    print(count)