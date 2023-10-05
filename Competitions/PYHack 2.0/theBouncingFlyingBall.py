class Flyball:

    def __init__(self,dx,dy,dz, p,q,r,L,W,H):
        self.position = [p,q,r]
        self.direction = [dx,dy,dz]
        self.box = [L,W,H]
        self.catched = False
        self.timeplayed = 0

    def detectCollision(self, playerPosition):
        if (self.position[0]<playerPosition[0] and playerPosition[0]<=self.position[0]+self.direction[0]) or (self.position[0]>playerPosition[0] and playerPosition[0]>=self.position[0]+self.direction[0]):
            if self.direction[0]==0:
                ratio_0 == float("inf")
            else:
                ratio_0 = (self.position[0]-playerPosition[0])/self.direction[0]
            if self.direction[1]==0:
                ratio_1 == float("inf")
            else:
                ratio_1 = (self.position[1]-playerPosition[1])/self.direction[1]
            if self.direction[2]==0:
                ratio_2 == float("inf")
            else:
                ratio_2 = (self.position[2]-playerPosition[2])/self.direction[2]
            if ratio_0==ratio_1 and ratio_0==ratio_2:
                self.catched = True
                return True
        return False

    def moveNext(self,Sergey,Chen,timeStart=0.0):
        if self.detectCollision(Sergey) or self.detectCollision(Chen):
            return None
        else:
            moveTime = 1.0-timeStart
            if self.direction[0]>=0:
                if self.direction[0] == 0:
                    ratio_0 = float("inf")
                else:
                    ratio_0 = (self.box[0]-self.position[0])/(self.direction[0]*moveTime)
            else:
                ratio_0 = (0-self.position[0])/(self.direction[0]*moveTime)
            if self.direction[1]>=0:
                if self.direction[1] == 0:
                    ratio_1 = float("inf")
                else:
                    ratio_1 = (self.box[1]-self.position[1])/(self.direction[1]*moveTime)
            else:
                ratio_1 = (0-self.position[1])/(self.direction[1]*moveTime)
            if self.direction[2]>=0:
                if self.direction[2] == 0:
                    ratio_2 = float("inf")
                else:
                    ratio_2 = (self.box[2]-self.position[2])/(self.direction[2]*moveTime)
            else:
                ratio_2 = (0-self.position[2])/(self.direction[2]*moveTime)

            moveThisTime = min(moveTime,ratio_0,ratio_1,ratio_2)

            self.position[0] += self.direction[0]*moveThisTime
            self.position[1] += self.direction[1]*moveThisTime
            self.position[2] += self.direction[2]*moveThisTime
            if moveThisTime == ratio_0:
                self.direction[0] = (-self.direction[0])
            if moveThisTime == ratio_1:
                self.direction[1] = (-self.direction[1])
            if moveThisTime == ratio_2:
                self.direction[2] = (-self.direction[2])
            
            
            if moveThisTime != moveTime:
                self.moveNext(Sergey,Chen,timeStart+moveThisTime)
        
        return None
                
T = int(input())

for _ in range(T):
    L,W,H,a,b,c,d,e,f,p,q,r,N = tuple(map(int,input().split()))
    Sergey = [a,b,c]
    Chen = [d,e,f]
    runTime = (2*N+1)**3
    balls = []
    answer = 0

    for i in range((-N),N+1):
        for j in range((-N),N+1):
            for k in range((-N),N+1):
                if i==0 and j==0 and k==0:
                    pass
                else:
                    balls.append(Flyball(i,j,k,p,q,r,L,W,H))

    for ball in balls:
        while ball.timeplayed < runTime and not ball.catched:
            ball.moveNext(Sergey,Chen)
            ball.timeplayed += 1
        if ball.catched:
            answer+=1

    print(answer)