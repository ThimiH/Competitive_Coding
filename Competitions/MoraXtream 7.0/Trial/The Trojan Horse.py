class DisJointSets():
    def __init__(self,N):
        # Initially, all elements are single element subsets
        self._parents = [node for node in range(N)]
        self._ranks = [1 for _ in range(N)]
    
    def find(self, u):
        while u != self._parents[u]: 
            # path compression technique
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return None
        self._parents[root_v] = root_u
        self._ranks[root_u] += self._ranks[root_v]
        self._ranks[root_v] = 0
        return None
    
N,P = tuple(map(int,input().split()))

DocPairs = DisJointSets(N)

for Pair in range(P):
    D1,D2 = tuple(map(int,input().split()))
    DocPairs.union(D1,D2)

answer = 0

for Count in DocPairs._ranks:
    if Count != 0:
        N-=Count
        answer += Count*N

print(answer)

# N,P = tuple(map(int,input().split()))

# solgrid = {}
# sollst = [a for a in range(N)]

# for i in range(N):
#     solgrid[i] = []

# for p in range(P):
#     x,y = tuple(map(int,input().split()))
#     solgrid[x].append(y)
#     solgrid[y].append(x)

# citycount = []

# while len(sollst)>0:
#     citycount.append(0)
#     sol = sollst[-1]
#     sollst = sollst[:-1]
#     citycount[-1]+=1
#     solq = []
#     for man in solgrid[sol]:
#         if man in sollst:
#             citycount[-1]+=1
#             solq.append(man)
#             sollst.remove(man)
#     while len(solq)>0:
#         sol = solq[-1]
#         solq = solq[:-1]
#         for man in solgrid[sol]:
#             if man in sollst:
#                 citycount[-1]+=1
#                 solq.append(man)
#                 sollst.remove(man)
    
# tot = 0
# ans = 0

# for n in citycount:
#     tot+=n
#     ans+=n*(N-tot)

# print(ans)