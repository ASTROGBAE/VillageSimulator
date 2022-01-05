

printed = True

def reportFounding(group):
    groupString = ""
    for person in group:
        groupString += ", " + person.name
    makeLog("Village has been founded by " + groupString)
    
def reportBirth(person):
    makeLog("Congratulations! " + person.parents[0].name + " and " + person.parents[1].name + " have given birth to " + person.name)
    
def reportMarriage(first, second):
    makeLog("Congratulations! " + first.name + " and " + second.name + " are married!")

def reportDeath(person):
    makeLog(person.name + " has passed away")

def makeLog(message):
    if printed: # todo: add IO for message, if printed or not
        print(message)