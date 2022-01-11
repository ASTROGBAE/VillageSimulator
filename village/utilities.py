# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:41:59 2021

@author: gabeb
"""

import random 


occupations = ["labour", "domestic", "idle"]

# param: proportion that this method will return True, False otherwise
def rollChance(proportion):
    chance = random.randint(0, 101) / 100
    if (chance <= proportion):
        return True
    return False 