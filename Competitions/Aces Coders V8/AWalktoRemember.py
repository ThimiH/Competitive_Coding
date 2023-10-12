C,E,N,S_0 = tuple(map(float,input().split()))
N = int(N)

TT = C/S_0
CC = 0

face_to_face = []

for _ in range(N):
    x,s= tuple(map(float,input().split()))
    if s>0:
        TT = max(TT,(C-x)/s)
    else:
        face_to_face.append((x,s))

for x,s in face_to_face:
    if x+TT*s<=C:
        CC += 1

print(round(TT),CC)