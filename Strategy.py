from enum import Enum

class StrategiesEnum(Enum):
    allC = 0
    allD = 1
    kC = 2
    kD = 3
    kDC=4

class Strategy:
    def __init__(self,stratEnum:StrategiesEnum,k:int ) -> None:
        self.Label=stratEnum
        self.K=k