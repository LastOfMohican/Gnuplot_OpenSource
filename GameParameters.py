
from enum import Enum
import GameParameters

class MapParameters:
    def __init__(self, rows:int,col:int, initC:float) -> None:
        self.Rows=rows
        self.Columns=col
        self.InitC=initC
        
    def getTestData():
        return MapParameters(
            90,90,0.5
        )    
           
class StrategiesParameters:
    def __init__(self, allC:float,allD:float,kD:float,kC:float,kDC:float,kFrom:int,kTo:int) -> None:
        self.AllC=allC
        self.AllD=allD
        self.KD=kD
        self.KC=kC
        self.KDC=kDC
        self.KFrom=kFrom
        self.KTo=kTo

    def getTestData():
        return StrategiesParameters(
            0.2,0.2,0.2,0.2,0.2,0,8
        )                     
class ComprtitionType(Enum):
    Roulette = 0
    Tournament = 1
    
    def getTestData():
        return ComprtitionType.Roulette    
class MutationParameters:
    def __init__(self, stateMut:float,stratMut:float,neighMut0:float,neighMut1:float) -> None:
        self.StateMut=stateMut
        self.StratMut=stratMut
        self.NeighMut0=neighMut0
        self.NeighMut1=neighMut1
        
    def getTestData():
        return MutationParameters(
            0.1,0.1,0.1,0.1
        )   
class DebugParameters(Enum):
    ReadState = 1
    ReadStrategy = 1
    
    def getTestData():
        return 1

class TestParameters(Enum):
    Test1 = 1
    Test2 = 2
    Test3 = 3   

    def getTestData():
        return [1,2]

class PlayoffParameters:
    def __init__(self, a:float,b:float,c:float,d:float) -> None:
        self.A=a
        self.B=b
        self.C=c
        self.D=d
    def getTestData():
        return PlayoffParameters(
            0.3,0.2,0.3,0.2
        )      
        
class GameParameters:
    def __init__(self, mapParameters: MapParameters, strategiesParameters:StrategiesParameters,sharing:bool,
                 comprtitionType:ComprtitionType, mutationParameters:MutationParameters,seed:int, num_of_iter:int,num_of_exper:int,
                debugParameters:list[DebugParameters],playoffParameters:PlayoffParameters,synchProlo:float,optimalNum1:int,testParameters:list[TestParameters]) -> None:
        self.MapParameters=mapParameters
        self.StrategiesParameters=strategiesParameters
        self.Sharing=sharing
        self.ComprtitionType=comprtitionType
        self.MutationParameters=mutationParameters
        self.Seed=seed
        self.num_of_iter=num_of_iter
        self.num_of_exper=num_of_exper
        self.DebugParameters=debugParameters
        self.PlayoffParameters=playoffParameters
        self.SynchProlo=synchProlo
        self.OptimalNum1=optimalNum1
        self.TestParameters=testParameters
        
    def getTestData()->GameParameters:
        return GameParameters(
            mapParameters=MapParameters.getTestData(),
            strategiesParameters=StrategiesParameters.getTestData(),
            sharing=True,
            comprtitionType=ComprtitionType.getTestData(),
            mutationParameters=MutationParameters.getTestData(),
            seed=890,
            num_of_iter=100,
            num_of_exper=1,
            debugParameters=DebugParameters.getTestData(),
            playoffParameters=PlayoffParameters.getTestData(),
            synchProlo=0.5,
            optimalNum1=676,
            testParameters=[1,2]
        )    
        
        

    