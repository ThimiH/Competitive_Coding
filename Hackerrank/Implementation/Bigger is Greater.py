def lexonxt(word):
    word = list(word)
    state = False
    for i in range(len(word)-2,-1,-1):
        l = word[i]
        w2 = word[i+1:]
        w2.sort()
        for let in w2:
            if let>l:
                w2.remove(let)
                w2.append(l)
                w2.sort() 
                return word[:i]+[let]+w2
    return 'no answer'

t = int(input())

for z in range(t):
    word = input()
    print(*lexonxt(word),sep='')