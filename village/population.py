import random

from event import Event

# TODO: move this!
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.occupation = "idle" # TODO: add functionality for this?


class Population(Event):
    def __init__(self, key, value):
        super().__init__(key, value)
        self.persons = []
        
    def changePersons(self, newVal):
        difference = newVal - len(self.persons)
        if difference != 0: # people have been born or died...
            if difference > 0: # people have been born
                for i in range(difference):
                    self.persons.append(Person("John Doe", "m", 27)) # TODO make person list, make more complicated?
            else: # people have died...
                for i in range(-1*difference):
                    if len(self.persons) != 0: # if not empty
                        del self.persons[0] # remove from end of list
        return 0
        
    # WARNING! have a seperate instance of random for this in multithreaded programs
    # for now, represents population increase/decrease
    # OVERRIDE of think in event parent class
    # update village object
    def think(self):
        newVal = self.value * int(random.gauss(0.4, 3))
        self.changePersons(newVal)
        return newVal