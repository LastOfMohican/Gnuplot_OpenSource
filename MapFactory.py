from GameParameters import *
from Map import Map
from Point import *
from Strategy import *
import numpy as np

import random
#
class MapFactory:
    def __init__(self ) -> None:
        pass
    def setMargines(self):
        for r in range(0,self.gameParameters.MapParameters.Rows+2):
            margin=self.gameParameters.MapParameters.Columns+1
            self.map.Matrix[r][0]=Point(r,0,1,Strategy(StrategiesEnum.allD,-1))
            self.map.Matrix[r][margin]=Point(r,margin,1,Strategy(StrategiesEnum.allD,-1))

        for c in range(0,self.gameParameters.MapParameters.Columns+2):
            margin=self.gameParameters.MapParameters.Rows+1
            self.map.Matrix[0][c]=Point(0,c,1,Strategy(StrategiesEnum.allD,-1))
            self.map.Matrix[margin][c]=Point(margin,c,1,Strategy(StrategiesEnum.allD,-1))

    def setStrategyAndState(self):
        StrategiesParameters=self.gameParameters.StrategeiesParameters
        options=[StrategiesEnum.allC,StrategiesEnum.allD,StrategiesEnum.kC,StrategiesEnum.kD,StrategiesEnum.kDC]
        probabilities=[StrategiesParameters.AllC,StrategiesParameters.AllD,StrategiesParameters.KC,StrategiesParameters.KD,StrategiesParameters.KDC]
        for r in range(1,self.gameParameters.MapParameters.Rows+1):
            for c in range(1,self.gameParameters.MapParameters.Columns+1):
                stratEnum=np.random.choice(options, p=probabilities)
                strat= Strategy(stratEnum,self.setK(stratEnum))
                state=int(self.gameParameters.MapParameters.InitC >= random.random())
                self.map.Matrix[r][c]= Point(r,c,state,strat)

    def setK(self,strat:StrategiesEnum):
        if strat == StrategiesEnum.allC or strat == StrategiesEnum.allD:
            return -1
        return random.randint(self.gameParameters.StrategeiesParameters.KFrom, self.gameParameters.StrategeiesParameters.KTo)

    def pepare8Group(self):
        for r in range(2,self.gameParameters.MapParameters.Rows-2):
            for c in range(2,self.gameParameters.MapParameters.Columns-2):
                point:Point=self.map.Matrix[r][c]
                if(not self.map.is8Group(point)):
                    continue
                if(point.State):
                    self.map.Group8_1.append(point)
                else:
                    self.map.Group8_0.append(point)

    def generateMapFromGameParameters(self,gameParameters:GameParameters) -> Map: 
        self.map= Map(gameParameters.MapParameters.Columns,gameParameters.MapParameters.Rows)
        self.gameParameters=gameParameters
        self.setMargines()
        self.setStrategyAndState()
        self.setMargines()
        self.pepare8Group()
        return self.map


    def generateMap(self,map:Map) -> Map:
        return  Map()