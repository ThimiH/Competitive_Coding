numOfRounds, numOfPlayers  = tuple(map(int,input().split()))

pointGrid = []

for _ in range(numOfRounds):
    pointGrid.append(list(map(int,input().split())))
    
print(pointGrid)

finalScores = list(map(int,input().split()))

def checkEven(list1, list2, length):
    for ind in range(1,length,2):
        if list1[ind]>list2[ind]:
            return False
    return True

def checkOdd(list1,list2,length):
    for ind in range(length,2):
        if list1[ind]>list2[ind]:
            return False
    return True

def addEven(list1, list2, length):
    for ind in range(1,length,2):
        list1[ind]+=list2[ind]
    return list1

def addOdd(list1, list2, length):
    for ind in range(length,2):
        list1[ind]+=list2[ind]
    return list1

def complete(list1,list2,length):
    for ind in range(length):
        if list1[ind]!=list2[ind]:
            return False
    return True

def wheelOfMayham(answer,roundsRemaining,currentScore):
    print(answer)
    global finalScores,numOfPlayers,numOfRounds,pointGrid
    if roundsRemaining==0:
        if complete(currentScore,finalScores,numOfPlayers):
            return answer
    else:
        if checkEven(currentScore,finalScores,numOfPlayers):
            if checkOdd(currentScore,finalScores,numOfPlayers):
                print(roundsRemaining)
                return wheelOfMayham(answer+'a',roundsRemaining-1,addOdd(addEven(currentScore,pointGrid[numOfRounds-roundsRemaining],numOfPlayers),pointGrid[numOfRounds-roundsRemaining],numOfPlayers))
            return wheelOfMayham(answer+'b',roundsRemaining-1,addEven(currentScore,pointGrid[numOfRounds-roundsRemaining],numOfPlayers))
        if checkOdd(currentScore,finalScores,numOfPlayers):
            return wheelOfMayham(answer+'c',roundsRemaining-1,addOdd(currentScore,pointGrid[numOfRounds-roundsRemaining],numOfPlayers))
    return "-1"

print(wheelOfMayham("",numOfRounds,[0]*numOfPlayers))