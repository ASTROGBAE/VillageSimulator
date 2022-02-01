# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:19:09 2021

@author: gabeb
"""

import population as pop, weather as wea, village as vil
from datetime import date, timedelta

# village event iterator
startDate = date.fromisoformat('0853-01-01')
events = [pop.Population(startDate), wea.Weather(startDate)] # TODO refactor starting date to make it better?
duration = timedelta(weeks=52*20)
town = vil.Village("Appleton", startDate)

for i in range(0, town.dateDiffToIt(duration)): # calculate by second, TODO work out how to deal with returning total seconds not equal?
    for event in events: # todo: make it so this affects a group of stats?
        workTicket = event.work((startDate + town.getItTimeDelta(i))) # think and log time 
        town.addVillageTicket(workTicket) # pass difference in ticket values, update stats
    
print("The end!")