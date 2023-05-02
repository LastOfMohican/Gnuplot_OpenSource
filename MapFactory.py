from GameParameters import *
from Map import Map
from Point import *
from Strategy import *
import numpy as np

import random


class MapFactory:
    def __init__(self) -> None:
        pass

    def setMargines(self):
        margin = self.C+1
        for r in range(0, self.R+2):
            self.map.Matrix[r][0].State=0
            self.map.Matrix[r][0].Strategy=Strategy(StrategiesEnum.allD, -1)
            self.map.Matrix[r][margin].State=0
            self.map.Matrix[r][margin].Strategy=Strategy(StrategiesEnum.allD, -1)

        margin = self.R+1
        for c in range(0, self.C+2):
            self.map.Matrix[0][c].State=0
            self.map.Matrix[0][c].Strategy=Strategy(StrategiesEnum.allD, -1)
            self.map.Matrix[margin][c].State=0
            self.map.Matrix[margin][c].Strategy=Strategy(StrategiesEnum.allD, -1)

    def setStrategyAndState(self):
        StrategiesParameters=self.gameParameters.StrategiesParameters
        options=[StrategiesEnum.allC,StrategiesEnum.allD,StrategiesEnum.kC,StrategiesEnum.kD,StrategiesEnum.kDC]
        probabilities=[StrategiesParameters.AllC,StrategiesParameters.AllD,StrategiesParameters.KC,StrategiesParameters.KD,StrategiesParameters.KDC]

        for r in range(1,self.R+1):
            for c in range(1,self.C+1):
                stratEnum=np.random.choice(options, p=probabilities)
                self.map.Matrix[r][c].State=int(self.gameParameters.MapParameters.InitC > random.random())
                self.map.Matrix[r][c].Strategy=Strategy(stratEnum,self.setK(stratEnum))

    def setK(self, strat: StrategiesEnum):
        if strat == StrategiesEnum.allC or strat == StrategiesEnum.allD:
            return 0
        return random.randint(self.gameParameters.StrategiesParameters.KFrom, self.gameParameters.StrategiesParameters.KTo)

    def pepare8Group(self):
        for r in range(1, self.R+1):
            for c in range(1, self.C+1):
                point: Point = self.map.Matrix[r][c]
                if (not self.map.is8Group(point)):
                    continue
                if (point.State):
                    self.map.Group8_1.append(point)
                else:
                    self.map.Group8_0.append(point)

    def generateMapFromGameParameters(self, gameParameters: GameParameters) -> Map:
        self.R=gameParameters.MapParameters.Rows
        self.C=gameParameters.MapParameters.Columns
        self.map = Map(self.C,self.R)
        self.map.Matrix=[[Point(x, y,0,Strategy(0,0)) for y in range(self.R+2)] for x in range(self.C+2)]
        self.gameParameters = gameParameters
        self.setMargines()
        self.setStrategyAndState()
        self.pepare8Group()
        return self.map

    def generateMap(self, map: Map) -> Map:
        return Map()
