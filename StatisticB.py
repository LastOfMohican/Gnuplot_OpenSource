
import StatisticB
class StatisticB:
    def __init__(self, iter: int, 
                 f_0D: float, f_1D: float, f_2D: float, f_3D: float, f_4D: float, f_5D: float, f_6D: float, f_7D: float, f_8D: float,
                 f_0C: float, f_1C: float, f_2C: float, f_3C: float, f_4C: float, f_5C: float, f_6C: float, f_7C: float, f_8C: float,
                 f_0DC: float, f_1DC: float, f_2DC: float, f_3DC: float, f_4DC: float, f_5DC: float, f_6DC: float, f_7DC: float, f_8DC: float
                 ) -> None:
        self.iter = iter

        self.f_0D = f_0D
        self.f_1D = f_1D
        self.f_2D = f_2D
        self.f_3D = f_3D
        self.f_4D = f_4D
        self.f_5D = f_5D
        self.f_6D = f_6D
        self.f_7D = f_7D
        self.f_8D = f_8D

        self.f_0C = f_0C
        self.f_1C = f_1C
        self.f_2C = f_2C
        self.f_3C = f_3C
        self.f_4C = f_4C
        self.f_5C = f_5C
        self.f_6C = f_6C
        self.f_7C = f_7C
        self.f_8C = f_8C

        self.f_0DC = f_0DC
        self.f_1DC = f_1DC
        self.f_2DC = f_2DC
        self.f_3DC = f_3DC
        self.f_4DC = f_4DC
        self.f_5DC = f_5DC
        self.f_6DC = f_6DC
        self.f_7DC = f_7DC
        self.f_8DC = f_8DC

    def getTestData() -> StatisticB:
        return StatisticB(
            0,
            0.0, 
            0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
            0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
            0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8
        )

    def toList(self):
        return [value for value in vars(self).values()]




