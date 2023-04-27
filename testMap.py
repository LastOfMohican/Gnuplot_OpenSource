from GameParameters import GameParameters
from Map import *
from Point import *
from Strategy import *
from MapFactory import MapFactory

gptd=GameParameters.getTestData()# tutaj podajcie z frontu

mapf=MapFactory()
map=mapf.generateMapFromGameParameters(gptd)

Matrix=map.toStateMatrixWithouMargines()
for el in Matrix:
    print(el)

Matrix=map.toStateMatrix()
for el in Matrix:
    print(el)
any=2