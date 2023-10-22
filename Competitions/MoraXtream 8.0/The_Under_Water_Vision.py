for _ in range(int(input())):
    input()
    temp = []
    for _ in range(50):
        temp = [input()]+temp
    density = [[0] for _ in range(50)]
    for line in temp:
        for i in range(50):
            density[i].append(density[i][-1]+int(line[i]))

    for line in range(50):
        for i,num in enumerate(density[line]):
            if i != 0:
                density[line][i]/=i

    grad = [[0]*50 for _ in range(50)]

    for i in range(50):
        for j in range(50):
            grad[i][j] = density[i][j]-density[i][j+1]

    seq = []
    for line in grad:
        seq.append(line.index(max(line)))
    
    print(seq)
            


