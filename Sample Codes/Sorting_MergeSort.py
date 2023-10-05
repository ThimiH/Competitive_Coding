#slowerrrrr or wrong

def pair(grid):
    length = len(grid)
    newgrid = []
    for i in range(0,length,2):
        newel = []
        el1 = grid[i]
        try:
            el2 = grid[i+1]
            while el1!=[] and el2!=[]:
                if el1[0]>=el2[0]:
                    newel.append(el2[0])
                    el2=el2[1:]
                else:
                    newel.append(el1[0])
                    el1=el1[1:]
            newel+=el1
            newel+=el2
            newgrid.append(newel)
        
        except:
            newgrid.append(el1)

    if len(newgrid)==1:
        return newgrid[0]
    else:
        return pair(newgrid)

def mergesort(numlst):
    pairlst = []
    length = len(numlst)
    for i in range(0,length,2):
        try:
            num1 = numlst[i]
            num2 = numlst[i+1]
            if num1>=num2:
                pairlst.append([num2,num1])
            else:
                pairlst.append([num1,num2])
        except:
            pairlst.append([numlst[i]])

    return pair(pairlst)

    



print(mergesort([5,6,8,10,1,13,0,4,7]))