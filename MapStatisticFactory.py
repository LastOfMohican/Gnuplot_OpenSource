from Map import *
from StatisticA import *
from StatisticB import *
from Statistic import *
from GameParameters import *
from Strategy import *
from Point import *
import numpy as np

class MapStatisticFactory:
    def __init__(self, map: Map, gameParameters: GameParameters, iter: int) -> None:
        self.Map = map
        self.Matrix = map.getMapWithoutMarginese()
        self.StrategyMatrix = [[0], [0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
        self.gameParameters = gameParameters
        self.iter = iter
        self.num_of_C = 0
        self.num_c_corr = 0

    def StatisticIteration(self, point: Point):
        self.num_of_C += point.State
        self.StrategyMatrix[point.Strategy.Label.value][point.Strategy.K] += 1
        self.num_c_corr += int(self.Map.isCorrect(point))

    def getStatistic(self) -> Statistic:
        R = self.Map.N
        C = self.Map.M
        for r in range(0, R):
            for c in range(0, C):       
                self.StatisticIteration(self.Matrix[r][c])


        num_of_kc=np.sum(self.StrategyMatrix[StrategiesEnum.kC.value])
        num_of_kd=np.sum(self.StrategyMatrix[StrategiesEnum.kD.value])
        num_of_kdc=np.sum(self.StrategyMatrix[StrategiesEnum.kDC.value])
        self.StatisticA = StatisticA(
            iter=self.iter,
            f_C=round(self.num_of_C/(C*R), 2),
            f_C_corr=round(self.resolveZero(self.num_c_corr,self.gameParameters.OptimalNum1), 2),
            av_pay=round(9, 2),  # na razie
            f_cr_0=round(len(self.Map.Group8_0)/(C*R), 2),
            f_cr_1=round(len(self.Map.Group8_1)/((C-2)*(R-2)), 2),
            f_allC=round(np.sum(self.StrategyMatrix[StrategiesEnum.allC.value])/(C*R), 2),
            f_allD=round(np.sum(self.StrategyMatrix[StrategiesEnum.allD.value])/(C*R), 2),
            f_Kd=round(num_of_kc/(C*R),  2),
            f_Kc=round(num_of_kd/(C*R),  2),
            f_Kdc=round(num_of_kdc/(C*R),  2),
            fstrat_ch=round(9, 2)  # na razie
        )
        kD=StrategiesEnum.kD.value
        kC=StrategiesEnum.kC.value
        kDC=StrategiesEnum.kDC.value
        sm=self.StrategyMatrix
        self.StatisticB = StatisticB(
            iter=self.iter, 
            f_0D=round(self.resolveZero(sm[kD][0],num_of_kd), 2), 
            f_1D=round(self.resolveZero(sm[kD][1],num_of_kd), 2), 
            f_2D=round(self.resolveZero(sm[kD][2],num_of_kd), 2),  
            f_3D=round(self.resolveZero(sm[kD][3],num_of_kd), 2), 
            f_4D=round(self.resolveZero(sm[kD][4],num_of_kd), 2), 
            f_5D=round(self.resolveZero(sm[kD][5],num_of_kd), 2), 
            f_6D=round(self.resolveZero(sm[kD][6],num_of_kd),2), 
            f_7D=round(self.resolveZero(sm[kD][7],num_of_kd), 2), 
            f_8D=round(self.resolveZero(sm[kD][8],num_of_kd), 2), 
            f_0C=round(self.resolveZero(sm[kC][0],num_of_kd), 2),
            f_1C=round(self.resolveZero(sm[kC][1],num_of_kd), 2), 
            f_2C=round(self.resolveZero(sm[kC][2],num_of_kd), 2),
            f_3C=round(self.resolveZero(sm[kC][3],num_of_kd), 2),
            f_4C=round(self.resolveZero(sm[kC][4],num_of_kd), 2),
            f_5C=round(self.resolveZero(sm[kC][5],num_of_kd), 2),
            f_6C=round(self.resolveZero(sm[kC][6],num_of_kd), 2),
            f_7C=round(self.resolveZero(sm[kC][7],num_of_kd), 2),
            f_8C=round(self.resolveZero(sm[kC][8],num_of_kd), 2),
            f_0DC=round(self.resolveZero(sm[kDC][0],num_of_kdc), 2), 
            f_1DC=round(self.resolveZero(sm[kDC][1],num_of_kdc), 2),  
            f_2DC=round(self.resolveZero(sm[kDC][2],num_of_kdc), 2), 
            f_3DC=round(self.resolveZero(sm[kDC][3],num_of_kdc), 2), 
            f_4DC=round(self.resolveZero(sm[kDC][4],num_of_kdc), 2), 
            f_5DC=round(self.resolveZero(sm[kDC][5],num_of_kdc), 2), 
            f_6DC=round(self.resolveZero(sm[kDC][6],num_of_kdc), 2), 
            f_7DC=round(self.resolveZero(sm[kDC][7],num_of_kdc), 2), 
            f_8DC=round(self.resolveZero(sm[kDC][8],num_of_kdc), 2)
            )
        return Statistic(self.StatisticA,self.StatisticB)
    def resolveZero(self,operator,canZero):
        if(not bool(canZero)):
            return 0
        return operator/canZero