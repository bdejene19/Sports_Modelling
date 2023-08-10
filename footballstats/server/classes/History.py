from array import array
from asyncio.windows_events import NULL
from numbers import Number
import numpy as np


class TeamHistory:
    def __init__(self, teamName: str, record: array(str)):
        self.name = teamName
        self.history = record

    def getAllHistory(self):
        return self.history

    def getHistoryWithin(self, startDate, endDate):
        if (endDate == NULL):
            return self.history[startDate:]

        return self.history[startDate:endDate]

    def getMostLosses(self):

        return
