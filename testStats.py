from GameParameters import GameParameters
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory
from MapStatisticFactory  import *
from StatisticA import *

gptd=GameParameters.getTestData()# tutaj podajcie z frontu

mapf=MapFactory()
map=mapf.generateMapFromGameParameters(gptd)
stf=MapStatisticFactory(map,gptd,0)
stat=stf.getStatistic()
la=stat.StatisticA.toList()
lb=stat.StatisticB.toList()
print(la)
print(lb)