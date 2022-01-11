# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

from population import Population
import village
from datetime import date, timedelta

# village event iterator
startDate = date.fromisoformat('0853-01-01')
events = [Population(startDate)] # TODO refactor starting date to make it better?
duration = timedelta(days=10)

for curSecond in range(0, int(duration.total_seconds())): # calculate by second, TODO work out how to deal with returning total seconds not equal?
    for event in events: 
        ticket = event.work((startDate + timedelta(seconds=curSecond))) # think and log time 
        village.stats[ticket[0]] += ticket[1] # update value (key, value)
    
print("The end!")