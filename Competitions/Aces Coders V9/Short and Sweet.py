t = int(input())
for i in range(t):
    v = int(input())
    if v==9:
        print("I'm participating in ACES Coders v9.0")
    elif v<9:
        print(f"I may have participated in ACES Coders v{v}.0")
    else:
        print(f"I will definitely try ACES Coders v{v}.0")