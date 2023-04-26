import MapStatistic 
import pathlib
class FileProvider:
    def __init__(self,path:str) -> None:
        self.Path=path
    def __init__(self) -> None:
        path=pathlib.Path().resolve()
        self.__init__(path)
        
    def WriteStatistic(self,mapStatics:list[MapStatistic.MapStatistic])->None:
        self.WriteToFile(str(x) for x in mapStatics)
    
    def WriteToFile(args:list[str],name:str)->None:
        file = open(name, "w")
        file.writelines(args)
        file.close()