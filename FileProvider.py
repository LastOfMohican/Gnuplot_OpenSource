from MapStatistic import *
import pathlib


class FileProvider:

    def __init__(self,name) -> None:
        path = pathlib.Path().resolve()
        self.Path = path
        self.Name = name
    def WriteStatisticsRange(self, mapStatics: list[MapStatistic]) -> None:
        file = open(self.Name, "a")
        for x in mapStatics:
            row=self.GetStrStatistic(x)
            file.write(row)
        file.close()
    def ClearFile(self):
        file = open(self.Name, "w")
        file.close()
    def GetStrStatistic(self, mapStatics: MapStatistic) -> str:
        return self.GetRow(10, mapStatics.toList())+"\n"

    def WriteToFile(self, args: list[str]) -> None:
        file = open(self.Name, "a")
        file.writelines(args)
        file.close()

   # def GetTitle(self) -> str:
  #      headers = ["iter", "f_C", "f_C_corr", "av_pay", "f_cr_0", "f_cr_1",
   #                "f_allC", "f_allD", "f_Kd", "f_Kc", "f_Kdc", "fstrat_ch"]
   #     return self.GetRow(10, headers)+"\n"
    def CreateTittle(self,obj) -> str:
        headers= obj.__dict__.keys()
        return self.GetRow(10, headers)+"\n"
    def GetRow(self, width: int, values: list):
        row = ""
        for value in values:
            row += f"{value:>{width}} "
        return row
