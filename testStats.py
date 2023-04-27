from GameParameters import GameParameters
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory
from MapStatisticFactory  import *
from MapStatistic import *

gptd=GameParameters.getTestData()# tutaj podajcie z frontu

mapf=MapFactory()
map=mapf.generateMapFromGameParameters(gptd)
stf=MapStatisticFactory(map,gptd)
stat=stf.getStatistic(0)
print(stat)