import State
import Strategy
class Point:
    def __init__(self,r:int,c:int,state:State,strat:Strategy):
        self.R=r
        self.C=c
        self.State=state
        self.Strategy=strat
        
    def setGlobalId(self,size:int):
        self.globalId= size*self.R+self.C
        