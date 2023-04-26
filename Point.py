import State
import Strategy
class Point:
    def __init__(self,x:int,y:int,state:State,strat:Strategy):
        self.X=x
        self.Y=y
        self.State=state
        self.Strategy=strat
        
    def setGlobalId(self,size:int):
        self.globalId= size*self.x
        