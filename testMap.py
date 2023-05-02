from GameParameters import GameParameters
from Map import *
from Point import *
from Strategy import *
from MapFactory import *

gptd=GameParameters.getTestData()# tutaj podajcie z frontu

mapf=MapFactory()
map=mapf.generateMapFromGameParameters(gptd)

# Matrix=map.toStrategyMatrix()
# for el in Matrix:
#     print(el)
# print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
# print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
Matrix=map.toAllMatrix()
print("STATE")
print("STATE")
for el in Matrix.States:
    print(el)

print("STRAT")
print("STRAT")
for el in Matrix.Strategies:
    print(el)

print("KD")
print("KD")
for el in Matrix.KDstrat:
    print(el)

print("KC")
print("KC")
for el in Matrix.KCstrat:
    print(el)


print("KDC")
print("KDC")
for el in Matrix.KDCstrat:
    print(el)

print("CDA")
print("CDA")
for el in Matrix.CDActions:
    print(el)
print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")





