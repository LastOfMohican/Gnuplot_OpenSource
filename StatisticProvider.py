import Map
import MapStatistic
class StatisticProvider:
    def __init__(self,map:Map) -> None:
        self.Map=map

    def getStatistic() -> MapStatistic:
        allC=1