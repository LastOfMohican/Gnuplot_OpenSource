import State
import Strategy
class Point:
    def __init__(self,r:int,c:int,state:State,strat:Strategy):
        self.R=r
        self.C=c
        self.State=state
        self.Strategy=strat
        
    def getGlobalId(self,size:int):
        self.globalId= (size*(self.R-1)+(self.C-1))+1
        