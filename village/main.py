# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

from population import Population
import village

# village event iterator
events = [Population(5)]
for day in range(0, 100): # testing for three days
    for event in events: 
        ticket = event.think()
        village.stats[ticket[0]] += ticket[1] # update value
    
print("The end!")