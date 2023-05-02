from GameParameters import *
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory
from MapStatisticFactory  import *
from StatisticA import *
from FileProvider import *
from GameProvider import *
from timeit import default_timer

start = default_timer()

# do stuff

gptd=GameParameters.getTestData()# tutaj podajcie z frontu
gp=GameProvider(gptd)
gp.InitGame()

duration = default_timer() - start
print(duration)