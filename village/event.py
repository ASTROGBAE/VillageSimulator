from datetime import timedelta
from temporal import Temporal

class Event(Temporal):
    
    def __init__(self, _keysToSet, _date):
        self.keysToSet = _keysToSet
        super().__init__(_date)
        
    # process done during each iteration, make sure to copy this to each new Event class
    def think(self, newDate):
        value = 0
        return value # returns (key, value)
        
    # think wrapper class to iterate through total iterations since last operation
    def work(self, newDate):
        workDict = {}
        for key in self.keysToSet:
            dateDifference = self.dateDiffToIt(newDate - self.date)
            totalWork = 0
            for i in range(0, int(dateDifference)): # do work based on difference in seconds since last log, TODO deal with the fact we are converint to int?
                curDate = newDate + self.getItTimeDelta(dateDifference) # uhhh how does this work, TODO fix date increments?
                self.date = curDate # update time
                totalWork += self.think(curDate) # log each new date
            workDict[key] = totalWork
        return workDict