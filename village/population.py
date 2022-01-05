import random

from event import Event
from person import Person


class Population(Event):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.persons = self.getInitialPopulation()
        self.graveyard = [] # todo make log output that doesn't need to be stored anymore
        self.partners = []
        
    def getInitialPopulation(self):
        init = []
        for x in range(0, random.randrange(2, 10)): # populate with 2-10 adults to begin withget
            init.append(Person(False))
        return init
    
    def updateDeaths(self):
        for person in self.persons:
            if person.naturalDeath(): # death by natural causes, bury in graveyard 
                self.persons.remove(person)
                self.graveyard.append(person)
    
    # create new persons based on 
    def updateBirths(self):
        for couple in self.partners:
            x = random.randrange(0, 100)
            if x < 5: # random chance for birth
                child = Person(True)
                child.parents = couple # record parents 
                self.persons.append(child) # birth new child at age zero, TODO make it more clear? 
    
    # update partners, if single, find a partner if available 
    def updatePartners(self):
        for first in self.persons:
            if first.age >= 16 and first.partner == None: # single and mature enough to have a partner TODO refactor!
                for second in self.persons:
                    if second.age >= 16 and first.sex != second.sex and second.partner == None and first != second: # single and mature enough to have a partner, not same person and not same sex
                        first.partner = second # mawwidge 
                        second.partner = first
                        self.partners.append([first, second])
        
    # WARNING! have a seperate instance of random for this in multithreaded programs
    # for now, represents population increase/decrease
    # OVERRIDE of think in event parent class
    # update village object
    def think(self):
        prevPop = len(self.persons)
        # update stuff...
        self.updatePartners()
        self.updateDeaths()
        self.updateBirths()
        return len(self.persons) - prevPop # return change in population 