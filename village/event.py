from datetime import timedelta
import ticket as tic
from temporal import Temporal

class Event(Temporal):
    
    def __init__(self, _keysToSet, _date):
        """abstract class to represent Event objects TODO look up how to actually make abstract??

        Args:
            _keysToSet ([type]): String list of village stats to update
            _date ([type]): current datetime object, used in comparisons for work
        """
        self.keysToSet = _keysToSet
        super().__init__(_date)
            
        
    
    # process done during each iteration, make sure to copy this to each new Event class
    def think(self, newDate, ticket): # TODO do you need to get a date?
        # for each ticket, do some sort of thinking...
        for key in self.keysToSet: ticket.setValue(key, 25);
        
    # think wrapper class to iterate through total iterations since last operation
    def work(self, newDate):
        returnTicket = tic.Ticket(self.keysToSet) # simple scoping, will be removed after use
        dateDifference = self.dateDiffToIt(newDate - self.date) # iterate through all increments since last log
        for i in range(0, int(dateDifference)): # do work based on difference in seconds since last log, TODO deal with the fact we are converint to int?
            self.think(self, newDate, returnTicket)
        return returnTicket
        