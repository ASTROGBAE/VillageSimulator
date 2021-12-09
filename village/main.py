# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

from simpleai.search import CspProblem, min_conflicts
import utilities

class Village:
    def __init__(self, name):
        self.name = name
        self.day = 0
        self.food = 10
        self.population = [Person("Greg", "M", 27), 
                           Person("James", "M", 6), Person("Mary", "F", 25)] # default population
        self.plots = [2, 1] # plot allotment: farm/house
    
    # CSP code for town council below...
    # constraint functions
    def constraint_enoughfood(self, variables, values): # for csp below
        if values.count("labour") >= len(variables): # enough food for everyone
            return 1
        return 0
    
    def constraint_surplusfood(self, variables, values): # for csp below
        if values.count("labour") > len(variables): # enough food for everyone
            return 1
        return 0
    
    def constraint_house(self, variables, values): # for csp below
        if values.count("domestic") >= self.plots[1]: # domestic per houses
            return 1 # 
        return 0

    def councilDecision(self):
        # csp problem
        # allocate jobs to persons based on if 
        names = [worker.name for worker in self.population]
        domains = dict([(name, utilities.occupations) for name in names])
        constraints = [(names, self.constraint_enoughfood),
            (names, self.constraint_surplusfood),
            (names, self.constraint_house)]
        
        problem = CspProblem(names, domains, constraints)
        result = min_conflicts(problem, initial_assignment=None, iterations_limit=100) # choose result with least conflicts
        return result # return for testing
        
    def updateDay(self):
        self.day += 1
        self.food = self.food - len(self.population)

        
class Person:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.occupation = "idle"
        
# main

town = Village("Appleton")
print(town.councilDecision())