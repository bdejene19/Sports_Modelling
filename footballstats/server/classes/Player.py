from array import array
from copyreg import constructor
from ctypes import Array
import matplotlib as mpl
import matplotlib.pyplot as plt


class BasePlayer:
    def __init__(self, name: str, nationality: str, shirtNum: float, generalStats: Array):
        self.name = name
        self.nationality = nationality
        self.leagueShirtNumber = shirtNum
        self.position = generalStats

    def getName(self):
        return self.name

    def getPosition(self):
        return self.position

    def changePositionTo(self, newPosition: str):
        self.position = newPosition


class PositionPlayer(BasePlayer):
    def __init__(self, name: str, nationality: str, shirtNum: float, generalStats: Array, positionStats: Array):
        super().__init__(name, nationality, shirtNum, generalStats)
        self.positionStats = positionStats

    def getPositionStats(self):
        return self.position

    def plotPositionStats(self, axisNames: array('u'), graphType: str, data: array):
        fig = plt.subplot()
        fig.plot()

        return
