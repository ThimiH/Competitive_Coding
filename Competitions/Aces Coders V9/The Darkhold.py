t = int(input())
cap = 'aeiou'
state = 'Easy'
for v in range(t):
    word = input()
    ind = 0
    for l in word:
        if l in cap:
            if ind>cap.index(l):
                ind =cap.index(l)
                state = 'Medium'
                break
    if state != 'Easy':
        ind = 4
        for l in word:
            if l in cap:
                if ind<cap.index(l):
                    ind =cap.index(l)
                    state = 'Hard'
                    break
    print(state)


