import random

from event import Event
from person import Person


class Population(Event):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.persons = []
        self.partners = []
        
    def changePersons(self, newVal): # TODO: make this more complicated? Add couples, change for birth and 
        difference = newVal - len(self.persons)
        if difference != 0: # people have been born or died...
            if difference > 0: # people have been born
                for i in range(difference):
                    self.persons.append(Person(False)) # TODO make person list, make more complicated?
            else: # people have died...
                for i in range(-1*difference):
                    if len(self.persons) != 0: # if not empty
                        del self.persons[0] # remove from end of list
        # testing string below
        #print("Daily population change (" + str(difference) + "): " + str(self.persons))
        return 0
        
    # WARNING! have a seperate instance of random for this in multithreaded programs
    # for now, represents population increase/decrease
    # OVERRIDE of think in event parent class
    # update village object
    def think(self):
        #newVal = int(self.value * random.gauss(0.4, 1)) removbed for testing
        newVal = 5
        self.changePersons(newVal)
        return newVal