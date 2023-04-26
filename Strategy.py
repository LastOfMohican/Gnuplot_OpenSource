from enum import Enum

class StrategiesEnum(Enum):
    allC = 0
    allD = 1
    kC = 2
    kD = 3
    kDC=4

class Strategy:
    def __init__(self,stratEnum:StrategiesEnum,k:int ) -> None:
        self.Lable=label
        self.K=k
    def __init__(self,stratEnum:StrategiesEnum) -> None:
        self.Lable=label
        self.K=None