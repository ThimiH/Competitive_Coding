#Complete this

numOfRounds, numOfPlayers  = tuple(map(int,input().split()))

point_grid = []

for _ in range(numOfRounds):
    point_grid.append(list(map(int,input().split())))

final_score = list(map(int,input().split()))

def op_a(current_score,round_scores):
    global numOfPlayers
    new_score = current_score
    for i in range(numOfPlayers):
        new_score[i] += round_scores[i]
    return new_score

def op_b(current_score,round_scores):
    global numOfPlayers
    new_score = current_score
    for i in range(1,numOfPlayers,2):
        new_score[i] += round_scores[i]
    return new_score

def op_c(current_score,round_scores):
    global numOfPlayers
    new_score = current_score
    for i in range(0,numOfPlayers,2):
        new_score[i] += round_scores[i]
    return new_score

def wheelofmayham(rounds,current_score):
    global final_score,point_grid
    if rounds == 1:
        if op_a(current_score,point_grid[-rounds])==final_score:
            return 'a'
        elif op_b(current_score,point_grid[-rounds])==final_score:
            return 'b'
        elif op_c(current_score,point_grid[-rounds])==final_score:
            return 'c'
        else:
            return ''
