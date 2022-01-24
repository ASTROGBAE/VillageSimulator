import random
import datetime

from event import Event
from person import Person
import log
import utilities


class Population(Event):
    def __init__(self, date):
        super().__init__(["population"], date) # define key and starting date
        self.graveyard = [] # todo make log output that doesn't need to be stored anymore
        self.partners = []
        self.persons = self.getInitialPopulation()
        
    # WARNING! have a seperate instance of random for this in multithreaded programs
    # for now, represents population increase/decrease
    # OVERRIDE of think in event parent class
    # update village object
    def think(self, newDate):
        prevPop = len(self.persons)
        # update stuff...
        self.updatePartners(newDate)
        self.updateDeaths(newDate)
        self.updateBirths(newDate)
        return len(self.persons) - prevPop # return change in population 
        
    def getInitialPopulation(self):
        init = []
        for x in range(1, random.randrange(2, 5)): # create couples
            couple = [Person(False, self.date), Person(False, self.date)] # TODO add option to make mature adult?, make sure male and female pairs?
            # TODO make persons more complicated so show birth date beforehand, add optional params?
            # add optional parameters to the above?
            init += couple
            self.partners.append(couple)
            if utilities.rollChance(0.3): # roll for children of couple
                child = Person(False, self.date)
                child.parents = couple
                init.append(child)
        for x in range(0, random.randrange(0, 3)): # populate with random adults without couples
            init.append(Person(False, self.date))
        log.reportFounding(self.date, init)
        return init
    
    def updateDeaths(self, newDate):
        # increment: once a 
        if self.persons != None and len(self.persons) != 0: # check if valid
            for person in self.persons:
                if person.naturalDeath(): # death by natural causes, bury in graveyard 
                    if person.partner != None:
                        person.partner.partner = None # remove couple status, if it exists
                        person.partner = None
                    self.persons.remove(person) # update death status
                    self.graveyard.append(person)
                    log.reportDeath(newDate, person)
    
    # create new persons based on 
    def updateBirths(self, newDate):
        if self.partners != None and len(self.partners) != 0: # check if valid
            for couple in self.partners:
                if self.yearlyChance((3/12 + 1)): # random chance for birth
                    child = Person(True, self.date)
                    child.parents = couple # record parents 
                    self.persons.append(child) # birth new child at age zero, TODO make it more clear? 
                    log.reportBirth(newDate, child)
    
    # update partners, if single, find a partner if available 
    def updatePartners(self, newDate):
        if self.persons != None and len(self.persons) > 1: # check if valid
            for first in self.persons:
                if self.yearlyChance((3)) and first.age >= 16 and first.partner == None: # single and mature enough to have a partner TODO refactor!, percentage to even check if they want to court
                    for second in self.persons:
                        if second.age >= 16 and first.sex != second.sex and second.partner == None and first != second: # single and mature enough to have a partner, not same person and not same sex
                            first.partner = second # mawwidge 
                            second.partner = first
                            self.partners.append([first, second])
                            log.reportMarriage(newDate, first, second)
                            break # found a partner, time to leave