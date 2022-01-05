import random 

class Person:
    def __init__(self, born):
        self.sex = random.choice(("M", "F"))
        self.name = self.genName(self.sex)
        if born == False:
            self.age = random.randrange(0, 60) # TODO: make this more complicated for choosing age?
        else: # if born, start as infant
            self.age = 0
        self.partner = None 
        self.parents = None 
        #self.stats = {"might":10, "wisdom":10, "health":10}
        #self.occupation = "idle" # TODO: add functionality for this?
        # TODO: implement cancelled stats above
        
    # returns true or false, based on if the character has died of a natural death
    # TODO very simplistic! simply trends that change of death increases a lot based on age (around 1 at 60 years)
    def naturalDeath(self):
        deathChanceCoefficient = 0.00025
        deathChance = deathChanceCoefficient * self.age * self.age
        roll = random.randrange(0, 100) / 100
        if (roll >= deathChance): return False # no chance of death
        return True 
        
        
    # return string of randomly generated name
    def genName(self, sex): 
        # TODO add to wrapper class that this pull from for names, instead of loading for literally every person...
        # LOADING algorithm, make more generic!
        # TODO add comments header that is ignored on readhing of all docuyents 
        name_prefix = []
        name_suffix = []
        if sex == "M": # male, choose male names
            f = open("village\\names_male.txt", "r")
        else: # == "F", female, choose female names
            f = open("village\\names_female.txt", "r")
        names = f.readlines() # iterate through all names (prefix and suffix)
        for name in names:
            if name[0] != " ": # if does not start with whitespace, it is a prefix
                name_prefix.append(name[0:-1]) # remove newline \n at the end
            else: # suffix if starts with whitespace, remove whitespace for stage
                name_suffix.append(name[1:-1]) # remove newline \n at the end with -1, remove whitespace with +1
        return random.choice(name_prefix) + random.choice(name_suffix) # choose a random prefix and suffix 
        # TODO: make random choice from list of strings a method in loader utility?
        # TODO: add all loaded assets into a single folder for .txt?? 