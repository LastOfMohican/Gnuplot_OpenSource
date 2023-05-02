from GameParameters import *
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory
from MapStatisticFactory  import *
from StatisticA import *
from StatisticB import *
from Statistic import *
from FileProvider import *

class GameProvider:
    def __init__(self,gameParameters:GameParameters ) -> None:
        self.MapList=[]
        self.iter=0
        self.gameParameters=gameParameters
        self.StatsA=[]
        self.StatsB=[]

    def InitGame(self):
        map=self.InitMap()
        self.MapList.append(map)
        
        self.PrepareStatistic()
        self.saveStatisticToFile()

    def PrepareStatistic(self):
        for x in self.MapList:
            stf=MapStatisticFactory(x,self.gameParameters,self.iter)
            stat=stf.getStatistic()
            self.StatsA.append(stat.StatisticA)
            self.StatsB.append(stat.StatisticB)
            self.iter+=1

    def InitMap(self)->Map:
        mapf=MapFactory()
        return mapf.generateMapFromGameParameters(self.gameParameters)

    def saveStatisticToFile(self):
        fp = FileProvider(self.gameParameters)
        fp.WriteStatisticARange(self.StatsA)
        fp.WriteStatisticBRange(self.StatsB)
