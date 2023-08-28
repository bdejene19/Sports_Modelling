from array import array
from ast import List
from asyncio.windows_events import NULL
from ctypes import Array
from numbers import Number
import numpy as np
import pandas as pd


class History:
    def __init__(self, history: str):
        self.history_df = pd.read_csv(history)

    def getAllHistory(self):
        return self.history_df

    def getN_head(self, numFromTop: Number):
        return self.history_df.head(numFromTop)

    def getN_tail(self, numFromBottom: Number):
        return self.history_df.tail(numFromBottom)

    def getColumnsByName(self, columns: array('u')):
        return self.history_df[0]  # need to come back for how to handle this

    def sortValuesByTime(self, isAscend: bool):
        return self.history_df.sort_values(by='DateTime column name', ascending=isAscend)


class LeagueHistory(History):
    def __init__(self, history: str, leagueName: str):
        super().__init__(history)
        self.name = leagueName

    def getLeague(self):
        return self.name


class TeamHistory(History):
    def __init__(self, history: str, teamName: str, history_filePath: str):
        super().__init__(history)
        self.name = teamName
        self.team_df = self.history_df[(
            self.history_df['Team Name'] == teamName
        )]

    def getTeamName(self):
        return self.name

    def getHistoryWithin(self, startDate, endDate):
        if (endDate == NULL):
            return self.team_df[startDate:]

        return self.team_df[startDate:endDate]

    def getMostLosses(self):

        return
