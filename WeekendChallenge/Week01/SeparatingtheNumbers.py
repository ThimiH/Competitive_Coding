q = int(input())

for _ in range(q):
    state = False
    string = str(input())
    for numLen in range(1,(len(string)//2)+1):
        beautiful = string[:numLen]
        number = int(beautiful)
        while len(beautiful) < len(string):
            number += 1
            beautiful = beautiful+str(number)

        if beautiful == string:
            print("YES",string[:numLen])
            state = True
    if not state:
        print("NO")