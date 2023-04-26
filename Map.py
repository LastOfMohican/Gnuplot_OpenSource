import Point
import Map
class Map:
    def __init__(self,N,M):
        self.N=N
        self.M=M
        self.Matrix=[[]]
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
        listNeighbours.append(self.Matrix[point.y-1][point.x-1])
        listNeighbours.append(self.Matrix[point.y-1][point.x])
        listNeighbours.append(self.Matrix[point.y-1][point.x+1])
        listNeighbours.append(self.Matrix[point.y][point.x+1])
        listNeighbours.append(self.Matrix[point.y+1][point.x+1])
        listNeighbours.append(self.Matrix[point.y+1][point.x])        
        listNeighbours.append(self.Matrix[point.y+1][point.x-1])    
        return listNeighbours
    