from array import array
from footballstats.server.classes.History import CoachHistory


class Coach(CoachHistory):
    def __init__(self, history: str, winRecord: array, goalRecord: array, name: str, team: str, playStyle: str, record: dict):
        super().__init__(history, winRecord, goalRecord)
        self.name = name
        self.team = team
        self.playStyle = playStyle
        self.coachingHistory = record

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getPlayStyle(self):
        return self.playStyle

    def updatePlayStyle(self, newPlayStyle: str):
        self.playStyle = newPlayStyle
