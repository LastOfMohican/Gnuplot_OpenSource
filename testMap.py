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
    print(el+"\n")
print("KD")
print("KD")
for el in Matrix.KDstrat:
    print(el+"\n")

print("KC")
print("KC")
for el in Matrix.KCstrat:
    print(el+"\n")


print("KDC")
print("KDC")
for el in Matrix.KDCstrat:
    print(el+"\n")

print("CDA")
print("CDA")
for el in Matrix.CDActions:
    print(el+"\n")
print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")





