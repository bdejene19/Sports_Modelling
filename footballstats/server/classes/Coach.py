class Coach:
    def __init__(self, name: str, team: str, playStyle: str,) -> None:
        self.name = name
        self.team = team
        self.playStyle = playStyle

    def getName(self):
        return self.name

    def getTeam(self):
        return self.team

    def getPlayStyle(self):
        return self.playStyle

    def updatePlayStyle(self, newPlayStyle: str):
        self.playStyle = newPlayStyle
