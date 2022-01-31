from datetime import timedelta
from temporal import Temporal

class Village(Temporal):
    
    # name of town and starting date
    def __init__(self, name, date):
        self.stats = {"name": name,
        "day": 0, "food": 10, "population": 5,
        "plots": {"farm":2, "house":1}}
        super().__init__(date)
    
    # get village statistics as a list
    def getStatsList(self, keyList):
        valueList = ()
        for key in keyList:
            valueList += [self.stats[key]]
        return valueList

    # get village plot statistic
    def getPlot(self, plot):
        return self.stats["plots"][plot]

    # set village statistic
    def setStats(self, statistic, value):
        self.stats[statistic] = value
        
    def updateDay(self): # TODO change to datetime with diff 
        self.stats["name"] += 1