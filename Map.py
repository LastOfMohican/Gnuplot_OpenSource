from Point import *
import Map
class Map:
    def __init__(self,N,M):
        self.N=N
        self.M=M
        self.Matrix=[[0 for x in range(N+2)] for y in range(M+2)] 
        self.Group8_0=[]
        self.Group8_1=[]
    def getNeighboursMap(self,point:Point) -> Map:
        mapNeighbours: Map = Map(3,3)
        listNeighbours:list =self.getNeighboursList(point)
        i=0
        for y in range(3):
            for x in range(3):
                mapNeighbours.Matrix[y,x]=listNeighbours[i]
                i+=1               
        return mapNeighbours
        
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

    def toStrategyMatrix(self):
        Matrix=[[0 for x in range(self.N+2)] for y in range(self.M+2)] 
        for x in range(self.M+2):
            for y in range(self.N+2):
                point=self.Matrix[x][y]
                Matrix[x][y]=point.Strategy.Label.value
        return Matrix

    def toStateMatrix(self):
        Matrix=[[0 for x in range(self.N+2)] for y in range(self.M+2)] 
        for x in range(self.M+2):
            for y in range(self.N+2):
                point=self.Matrix[x][y]
                Matrix[x][y]=point.State
        return Matrix

    def toStrategyMatrixWithouMargines(self):
        Matrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        for x in range(M):
            for y in range(N):
                point=self.Matrix[x+1][y+1]
                Matrix[x][y]=point.Strategy.Label.value
        return Matrix
        
    def toStateMatrixWithouMargines(self):
        Matrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        for x in range(self.M):
            for y in range(self.N):
                point=self.Matrix[x+1][y+1]
                Matrix[x][y]=point.State
        return Matrix

    def getMapWithoutMarginese(self):
        Matrix=[[0 for x in range(self.N)] for y in range(self.M)] 
        for x in range(self.M):
            for y in range(self.N):
                point=self.Matrix[x+1][y+1]
                Matrix[x][y]=point
        return Matrix