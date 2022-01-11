from datetime import date, timedelta

printed = True

def strDate(date):
    return str(date) + ': '

def reportFounding(date, group):
    groupString = ""
    for person in group:
        groupString += ", " + person.name
    makeLog(strDate(date) + "Village has been founded by " + groupString)
    
def reportBirth(date, person):
    makeLog(strDate(date) + "Congratulations! " + person.parents[0].name + " and " + person.parents[1].name + " have given birth to " + person.name)
    
def reportMarriage(date, first, second):
    makeLog(strDate(date) + "Congratulations! " + first.name + " and " + second.name + " are married!")

def reportDeath(date, person):
    makeLog(strDate(date) + person.name + " has passed away")

def makeLog(message):
    if printed: # todo: add IO for message, if printed or not
        print(message)