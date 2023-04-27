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
        num_c_corr=0
        num_Of_C=0
        for r in range(0,self.Map.N):
            for c in range(0,self.Map.M):
                point=self.Matrix[r][c]
                if(point.State ==1):
                    num_Of_C+=1
                strat=point.Strategy.Label.value
                self.StrategyMatrix[strat]+=1
                if(self.Map.isCorrect(point)):
                    num_c_corr+=1

        C=self.Map.N
        R=self.Map.M
        f_C= num_Of_C/(C*R)
        cr1=len(self.Map.Group8_1)/((C-2)*(R-2))

        return MapStatistic(
        iter=iter, 
        f_C=round(f_C,2), 
        f_C_corr= round(num_c_corr/self.gameParameters.OptimalNum1,2),#len(self.Map.Group8_1),#f_C#round(abs(num_Of_C-f_C)/self.gameParameters.OptimalNum1,2), #
        av_pay=round( 9,2), #na razie
        f_cr_0=round(len(self.Map.Group8_0)/(C*R),2),
        f_cr_1=round(len(self.Map.Group8_1)/((C-2)*(R-2)),2),
        f_allC=round(self.StrategyMatrix[StrategiesEnum.allC.value]/(C*R), 2),
        f_allD=round(self.StrategyMatrix[StrategiesEnum.allD.value]/(C*R), 2),
        f_Kd=round(self.StrategyMatrix[StrategiesEnum.kC.value]/(C*R),  2),
        f_Kc=round(self.StrategyMatrix[StrategiesEnum.kD.value]/(C*R),  2),
        f_Kdc=round(self.StrategyMatrix[StrategiesEnum.kDC.value]/(C*R),  2),
        fstrat_ch=round(9,2)#na razie
        )