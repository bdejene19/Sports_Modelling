import array
from ctypes import Array
from server.classes.Coach import Coach
from server.classes.Player import PositionPlayer


class Team:
    def __init__(self, name: str, league: str, coach: Coach, squad: array(PositionPlayer)):
        self.name = name
        self.league = league
        self.coach = coach
        self.squad = squad

    def getName(self):
        return self.name

    def getSquad(self):
        return self.squad

    def getLeague(self):
        return self.league

    def getCoach(self):
        return self.coach

    def getDefenders(self):
        return list(filter(lambda position: position == "Def"))

    def getMidfielders(self):
        return list(filter(lambda position: position == "Mid"))

    def getForwards(self):
        return list(filter(lambda position: position == "For"))

    def addPlayer(self, playerAdd: PositionPlayer):
        self.squad = (self.squad).push(playerAdd)

    def removePlayer(self, playerRemove: PositionPlayer):
        filtered = [player for player in self.squad if player != playerRemove]
        self.squad = filtered
