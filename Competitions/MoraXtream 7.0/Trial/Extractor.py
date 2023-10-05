#highly looping

'''
sent = input()

l = len(sent)

def finderl(word):
    if len(word) == 0:
        return 0
    if len(word) == 1 :
        return 1
    l = word[-1]
    word = word[:-1]
    for i in range(len(word)):
        if word[i]==l:
            word = word[i+1:]
            if len(word) == 0:
                return finderl(word)
            if word[0]==word[-1]:
                return (2 + finderl(word))
            else:
                return(2+max(finderl(word[i+1:]),finderl(word[i+1:][::-1])))
    
    return(finderl(word))


print(max(finderl(sent),finderl(sent[::-1])))

'''