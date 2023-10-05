inp = str(input()).split()

str1 = inp[0].lower()
str2 = inp[1].lower()

alp = 'abcdefghijklmnopqrstuvwxyz'
state = 'No'

for let in alp:
    if let in str1:
        if let in str2:
            state = 'Yes'
            break

print(state)
