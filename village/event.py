from datetime import timedelta
from temporal import Temporal

class Event(Temporal):
    
    def __init__(self, villageStat, date):
        self.villageStat = villageStat
        super().__init__(date)
        
    def think(self, newDate):
        value = 0
        return value # returns (key, value)
        
    # think wrapper class to iterate through total iterations since last operation
    def work(self, newDate):
        dateDifference = self.dateDiffToIt(newDate - self.date)
        totalWork = 0
        for i in range(0, int(dateDifference)): # do work based on difference in seconds since last log, TODO deal with the fact we are converint to int?
            curDate = newDate + self.getItTimeDelta(dateDifference) # uhhh how does this work, TODO fix date increments?
            self.date = curDate # update time
            totalWork += self.think(curDate) # log each new date
        return (self.villageStat, totalWork)