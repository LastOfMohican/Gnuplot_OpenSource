
from enum import Enum
import GameParameters
class MapParameters:
    def __init__(self, rows:int,col:int, initC:float) -> None:
        self.Rows=rows
        self.Columns=col
        self.InitC=initC
        
    def getTestData():
        return MapParameters(
            #test data
            #TO DO MACIEJ 
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
            #test data
            #TO DO MACIEJ 
        )                     
class ComprtitionType(Enum):
    Roulette = 0
    Tournament = 1
    
    def getTestData():
        return ComprtitionType(
            #test data
            #TO DO MACIEJ 
        )        
class MutationParameters:
    def __init__(self, stateMut:float,stratMut:float,neighMut0:float,neighMut1:float) -> None:
        self.StateMut=stateMut
        self.StratMut=stratMut
        self.NeighMut0=neighMut0
        self.NeighMut1=neighMut1
        
    def getTestData():
        return MutationParameters(
            #test data
            #TO DO MACIEJ 
        )   
class DebugParameters(Enum):
    ReadState = 0
    ReadStrategy = 1
    
    def getTestData():
        return DebugParameters(
            #test data
            #TO DO MACIEJ 
        )   
class TestParameters(Enum):
    Test1 = 1
    Test2 = 2
    Test3 = 3
    
    def getTestData():
        return list[TestParameters](
            #test data
            #TO DO MACIEJ 
        )   
class PlayoffParameters:
    def __init__(self, a:float,b:float,c:float,d:float) -> None:
        self.A=a
        self.B=b
        self.C=c
        self.D=d
    def getTestData():
        return PlayoffParameters(
            #test data
            #TO DO MACIEJ 
        )      
        
class GameParameters:
    def __init__(self, mapParameters: MapParameters, strategeiesParameters:StrategiesParameters,sharing:bool,
                 comprtitionType:ComprtitionType, mutationParameters:MutationParameters,seed:int, 
                debugParameters:list[DebugParameters],playoffParameters:PlayoffParameters,synchProlo:float,optimalNum1:int,testParameters:list[TestParameters]) -> None:
        self.MapParameters=mapParameters
        self.StrategeiesParameters=strategeiesParameters
        self.Sharing=sharing
        self.ComprtitionType=comprtitionType
        self.MutationParameters=mutationParameters
        self.Seed=seed
        self.DebugParameters=debugParameters
        self.PlayoffParameters=playoffParameters
        self.SynchProlo=synchProlo
        self.OptimalNum1=optimalNum1
        self.TestParameters=testParameters
        
    def getTestData()->GameParameters:
        return GameParameters(
            MapParameters.getTestData(),
            StrategiesParameters.getTestData(),
            True,
            ComprtitionType.getTestData(),
            MutationParameters.getTestData(),
            890,
            PlayoffParameters.getTestData(),
            1.0,
            676,
            TestParameters.getTestData()
        )    
        
        

    