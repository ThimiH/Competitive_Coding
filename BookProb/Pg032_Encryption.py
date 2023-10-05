vow = [x for x in 'aeiou']
con = [x for x in 'bcdfghjklmnpqrstvwxyz']

T = int(input())
inp = []

for y in range(T):
    inp.append([x for x in str(input())])

def check(inp):
    for lst in inp:
        if len(lst)>=5*10**4:
            return False
    return True
    
if check(inp):
    for lst in inp:
        vowcount = dict({x:0 for x in vow})
        concount = dict({x:0 for x in con})
        word = ''
        for let in lst:
            if let in vow:
                word += con[(vowcount[let]*5+vow.index(let))%21]
                vowcount[let]+=1
            else:
                word += vow[(concount[let]*21+con.index(let))%5]
                concount[let]+=1
        print(word)