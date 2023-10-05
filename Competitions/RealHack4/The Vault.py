class PassCode():
    def __init__(self,length,data):
        self.grid = [[1]*10 for _ in range(length)]
        self.possible = [10 for _ in range(length)]
        self.data = [["",0] for _ in range((data))]
        self.used = []
        self.length = length

    def zeros(self):
        index = 0
        for dat in self.data:
            if dat[1] == 0:
                self.used = 1
                for num in range(self.length):
                    if self.grid[num][int(dat[0][num])]==1:
                        self.possible[num]-=1
                    self.grid[num][int(dat[0][num])]=0
            index += 1

PW = PassCode(12,int(input()))
PW.used = [0*len(PW.data)]

for _ in range(len(PW.data)):
    string,correct = input().split()
    PW.data[_][0]=string
    PW.data[_][1]=int(correct)

print(PW.data)
print(PW.length)

while 0 in PW.used:
    PW.zeros()

print(PW.possible)
