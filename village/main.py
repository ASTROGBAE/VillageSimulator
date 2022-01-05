# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

from population import Population

# village event iterator
events = [Population("population", 5)]
for day in (1,2,3,4,5): # testing for three days,
    for event in events: event.processEvent()