# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

from population import Population

# village event iterator
events = [Population("population", 5)]

for event in events: event.processEvent()