from copyreg import constructor
from ctypes import Array


class BasePlayer:
    def __init__(self, name: str, nationality: str, shirtNum: float, generalStats: Array) -> None:
        self.name = name
        self.nationality = nationality
        self.shirtNumber = shirtNum
        self.position = generalStats

    def getName(self) -> str:
        return self.name

    def getPosition(self) -> str:
        return self.position

    def changePositionTo(self, newPosition: str) -> None:
        self.position = newPosition


class PositionPlayer(BasePlayer):
    def __init__(self, name: str, nationality: str, shirtNum: float, generalStats: Array, positionStats: Array) -> None:
        super().__init__(name, nationality, shirtNum, generalStats)
        self.positionStats = positionStats
