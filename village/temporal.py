from datetime import date, timedelta
import random

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
    # smallest increment possible of accuracy specified in variable below, represents number of decimal places
    # TODO removed random roll, get rid of this overall?
    def yearlyChance(self, proportion):
        accuracy = 10
        secProportion = proportion / self.yearToSec # proportion per second that chance occures
        proportionPerYear = random.randrange(0, pow(10, accuracy)) / pow(10, accuracy) # random proportion with a dicimal place of number equal to accuracy
        if proportionPerYear <= secProportion: # chance success
            return True
        return False # failure