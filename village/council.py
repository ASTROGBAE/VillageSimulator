# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:48:23 2021

@author: gabeb
"""

# todo
# implement greedy algorithm instead with new key function
# fix village stats for village import

import village

# CSP code for town council below...
# constraint functions
def constraint_enoughfood(variables, values): # for csp below
    if values.count("labour") >= len(variables): # enough food for everyone
        return 1
    return 0

def constraint_surplusfood(variables, values): # for csp below
    if values.count("labour") > len(variables): # enough food for everyone
        return 1
    return 0

def constraint_house(variables, values): # for csp below
    if values.count("domestic") >= village.getPlot("house"): # domestic per houses
        return 1 # 
    return 0

def councilDecision():
    # csp problem
    # allocate jobs to persons based on if 
    names = [worker.name for worker in population] # implement village in this
    domains = dict([(name, utilities.occupations) for name in names])
    constraints = [(names, constraint_enoughfood),
        (names, constraint_surplusfood),
        (names, constraint_house)]
    
    problem = CspProblem(names, domains, constraints)
    result = min_conflicts(problem, initial_assignment=None, iterations_limit=100) # choose result with least conflicts
    return result # return for testing