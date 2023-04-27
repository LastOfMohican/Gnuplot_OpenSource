from GameParameters import *
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory
from MapStatisticFactory  import *
from MapStatistic import *
from FileProvider import *

class GameProvider:
    def __init__(self,gameParameters:GameParameters ) -> None:
        self.MapList=[]
        self.iter=0
        self.gameParameters=gameParameters
        self.Stats=[]

    def InitGame(self):
        map=self.InitMap()
        self.MapList.append(map)
        
        self.PrepareStatistic()
        self.saveStatisticToFile("results.txt")

    def PrepareStatistic(self):
        for x in self.MapList:
            stf=MapStatisticFactory(x,self.gameParameters)
            stat=stf.getStatistic(self.iter)
            self.Stats.append(stat)
            self.iter+=1

    def InitMap(self)->Map:
        mapf=MapFactory()
        return mapf.generateMapFromGameParameters(self.gameParameters)

    def saveStatisticToFile(self,fileName:str):
        fp = FileProvider(fileName)
        fp.ClearFile()
        fp.WriteToFile([fp.GetTitle()])
        fp.WriteStatisticsRange(self.Stats)
