n = int(input())

notes = [0,0,0,0]
notes[0]=n//100

if notes[0]%5==0:
    notes[1]=notes[0]//5-1
    notes[0]=5
else:
    notes[1]=notes[0]//5
    notes[0]=notes[0]%5

if notes[1]>2:
    if notes[1]%2==0:
        notes[2]=notes[1]//2-1
        notes[1]=2
    else:
        notes[2]=notes[1]//2
        notes[1]=notes[1]%2

if notes[2]>5:
    if notes[2]%5==0:
        notes[3]=notes[2]//5-1
        notes[2]=5
    else:
        notes[3]=notes[2]//5
        notes[2]=notes[2]%5

for note in notes:
    print(note,end=" ")