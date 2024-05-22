simp_cap = ord('a')-ord('A')

decrypted = ['cjlv','U iuxx nq mf ftq eqzmfq fapmk fa tqmd m bqfufuaz rday Fuxxuge. Omeeuge mzp Ndgfge tmhq nqqz mofuzs efdmzsq. Etagxp nq nmow uz fuyq rad puzzqd.']
encrypted = ['qxzj','I will be at the senate today to hear a petition from Tillius. Cassius and Brutus have been acting strange. Should be back in time for dinner.']

code = {}

for i in range(len(decrypted)):
    d = decrypted[i]
    e = encrypted[i]
    for ind,letter in enumerate(d):
        if ord('a')<=ord(letter)<=ord('z'):
            code[letter] = e[ind]
            code[chr(ord(letter)-simp_cap)] = chr(ord(e[ind])-simp_cap)
        elif ord('A')<=ord(letter)<=ord('Z'):
            code[letter] = e[ind]
            code[chr(ord(letter)+simp_cap)] = chr(ord(e[ind])+simp_cap)
        else:
            code[letter] = e[ind]

for letter in input():
    try:
        print(code[letter], end='')
    except:
        print(letter,end='')