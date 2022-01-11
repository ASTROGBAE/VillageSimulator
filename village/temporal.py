from datetime import date, timedelta

from utilities import rollChance 

# class defining all child class that rely on a spatial dimension (change in time)

class Temporal():

    def __init__(self, date):
        self.date = date # date of last log
        #coefficient for translating a daily chance to seconds
        self.yearToSec = self.calcYeartoSeconds(self.date) # TODO calculate this every new year, year could change? 
        
    # return total seconds in the year, for use in probability
    def calcYeartoSeconds(self, currDate):
        curYear = currDate.year
        #if (curYear < 1000): # 3 digits, need to put a '0' in front of the string for formatting 
            #curYear = '0' + str(currDate.year)
        #else:
            #curYear = str(currDate.year)
        #dateStrStart = date.fromisoformat(curYear + '-01-01')
        #dateStrEnd = date.fromisoformat(curYear + '-12-31')
        #return (dateStrEnd- dateStrStart).total_seconds()
        return timedelta(weeks=52).total_seconds()
    
    # takes proportion per year of chance, return chance by second of occurance 
    def yearlyChance(self, proportion):
        secProportion = proportion * (1 / self.yearToSec)
        return rollChance(secProportion)