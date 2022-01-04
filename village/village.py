# singleton Village object

stats = {}
def __init__(name):
    stats["name"] = name
    stats["day"] = 0
    stats["food"] = 10
    stats["population"] = 5
    stats["plots"] = {"farm":2, "house":1}
    
# get village statistic
def getStat(statistic):
    return stats[statistic]

# get village plot statistic
def getPlot(plot):
    return stats["plots"][plot]

# set village statistic
def setStat(statistic, value):
    stats[statistic] = value
    
def updateDay(): # TODO change to datetime with diff 
    stats["name"] += 1