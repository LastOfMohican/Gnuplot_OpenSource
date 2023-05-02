from Point import *
from Strategy import *
from StrategyMatrix import *
import Map
class Map:
    def __init__(self,N,M):
        self.N=N
        self.M=M
        self.Matrix=[[0 for x in range(N+2)] for y in range(M+2)] 
        self.Group8_0=[]
        self.Group8_1=[]
        
    def getNeighboursList(self,point:Point) -> list: 
        listNeighbours:list =[]   
        listNeighbours.append(self.Matrix[point.R-1][point.C])
        listNeighbours.append(self.Matrix[point.R-1][point.C+1])
        listNeighbours.append(self.Matrix[point.R][point.C+1])
        listNeighbours.append(self.Matrix[point.R+1][point.C+1])
        listNeighbours.append(self.Matrix[point.R+1][point.C])    
        listNeighbours.append(self.Matrix[point.R+1][point.C-1]) 
        listNeighbours.append(self.Matrix[point.R][point.C-1])
        listNeighbours.append(self.Matrix[point.R-1][point.C-1])      
        return listNeighbours

    def is8Group(self,point:Point) -> bool:
        n=self.getNeighboursList(point)
        return (all(x.State == 1 for x in n) and point.State==1) or (all(x.State == 0 for x in n) and point.State==0)
    def isCorrect(self,point:Point)->bool:
        n=self.getNeighboursList(point)
        return all(x.State == 0 for x in n) and point.State==1

    def isCorrectPoint(self,point:Point):
        if(bool(point.State)):
            return self.isCorrect(point)
        n=list(map(lambda x: int(x.State),self.getNeighboursList(point)))
        ncount=n.count(1)
        return ( ncount==2 and  ((bool(n[0])  and bool(n[4])) or (bool(n[2])  and bool(n[6])) or 
        (ncount == 4 or ( bool(n[1])  and bool(n[3])  and bool(n[5])  and bool(n[7]) ) ) ) )    

    def toCDAction(self,point:Point):
        return int(self.isCorrectPoint(point))
    def toStrat(self,point:Point):
        return point.Strategy.Label    
    def toState(self,point:Point):
        return point.State
    def tokStrat(self,point:Point,strat):
        if(self.toStrat(point)==strat):
            return point.Strategy.K
        return 0

    def toAllMatrix(self):
        StateMatrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        StratMatrix=[[0 for x in range(self.N)] for y in range(self.M)]
        CDActionsMatrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        kDStratMatrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        kCStratMatrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        kDCStratMatrix=[[0 for x in range(self.N)] for y in range(self.M)]      
        for x in range(self.M):
            for y in range(self.N):
                point=self.Matrix[x+1][y+1]
                StateMatrix[x][y]=self.toState(point)
                StratMatrix[x][y]=self.toStrat(point).value
                CDActionsMatrix[x][y]=self.toCDAction(point)
                kDStratMatrix[x][y]=self.tokStrat(point, StrategiesEnum.kD)
                kCStratMatrix[x][y]=self.tokStrat(point, StrategiesEnum.kC)
                kDCStratMatrix[x][y]=self.tokStrat(point, StrategiesEnum.kDC)

        return StrategyMatrix(StateMatrix, StratMatrix, kDStratMatrix, kCStratMatrix, kDCStratMatrix, CDActionsMatrix)        

    def getMapWithoutMarginese(self):
        Matrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        for x in range(self.M):
            for y in range(self.N):
                point=self.Matrix[x+1][y+1]
                Matrix[x][y]=point
        return Matrix