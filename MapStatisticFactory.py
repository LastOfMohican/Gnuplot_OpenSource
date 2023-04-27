from Map import *
from MapStatistic import *
from GameParameters import *
from Strategy import *
class MapStatisticFactory:
    def __init__(self,map:Map,gameParameters:GameParameters) -> None:
        self.Map=map
        self.Matrix=map.getMapWithoutMarginese()
        self.StrategyMatrix=[0,0,0,0,0]
        self.gameParameters=gameParameters
    def getStatistic(self,iter:int) -> MapStatistic:
        num_Of_C=0
        for r in range(0,self.Map.N):
            for c in range(0,self.Map.M):
                if(self.Matrix[r][c].State ==1):
                    num_Of_C+=1
                strat=self.Matrix[r][c].Strategy.Label.value
                self.StrategyMatrix[strat]+=1
        C=self.Map.N
        R=self.Map.M
        f_C= num_Of_C/(C*R)
        return MapStatistic(
        iter=iter, 
        f_C=f_C, 
        f_C_corr=bs(num_Of_C-f_C)/self.gameParameters.OptimalNum1, #
        av_pay=1, #na razie
        f_cr0=len(self.Map.Group8_0),
        f_cr_1=len(self.Map.Group8_1),
        f_allC=self.StrategyMatrix[StrategiesEnum.allC.value]/(C*R), 
        f_allD=self.StrategyMatrix[StrategiesEnum.allD.value]/(C*R), 
        f_Kd=self.StrategyMatrix[StrategiesEnum.kC.value]/(C*R),  
        f_Kc=self.StrategyMatrix[StrategiesEnum.kD.value]/(C*R),  
        f_Kdc=self.StrategyMatrix[StrategiesEnum.kDC.value]/(C*R),  
        fstrat_ch=1.0#na razie
        )