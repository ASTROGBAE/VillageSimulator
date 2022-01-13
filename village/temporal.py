from datetime import date, timedelta
import random

from utilities import rollChance 

# class defining all child class that rely on a spatial dimension (change in time)

class Temporal():

    def __init__(self, date):
        self.date = date # date of last log
        #coefficient for translating a chance to the chosen time duration
        self.granularity = self.calcGranularity() # TODO calculate this every new year, year could change? 
        
    # define the granularity of the world below
    # 1 = seconds, 2 = hours, 3 >= days TODO add more options???
    granularityOption = 3
    
    def calcGranularity(self):
        if self.granularityOption == 1:
            return timedelta(weeks=52).total_seconds()
        elif self.granularityOption == 2:
            return timedelta(weeks=52).total_seconds()//3600
        return timedelta(weeks=52).days
    
    # return number of iterations diff between two dates, dif is timedelta
    def dateDiffToIt(self, diffDate): 
        if self.granularity == 1:
            return diffDate.total_seconds()
        elif self.granularity == 2:
            return diffDate.total_seconds()//3600
        return diffDate.days
    
    # return timedelta of difference in int, based on gradulatiy 
    def getItTimeDelta(self, diffInt):
        if self.granularity == 1:
            return timedelta(seconds=diffInt)
        elif self.granularity == 2:
            return timedelta(hours=diffInt)
        return timedelta(days=diffInt)
    
    # takes proportion per granularity of chance, return chance by second of occurance 
    # smallest increment possible of accuracy specified in variable below, represents number of decimal places
    # TODO removed random roll, get rid of this overall?
    def yearlyChance(self, proportion):
        accuracy = 10
        secProportion = proportion / self.granularity # proportion per second that chance occures
        proportionPerGran = random.randrange(0, pow(10, accuracy)) / pow(10, accuracy) # random proportion with a dicimal place of number equal to accuracy
        if proportionPerGran <= secProportion: # chance success
            return True
        return False # failure