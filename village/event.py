import village

class Event():
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    # event run, will return the value, wrapper of think
    def processEvent(self):
        village.stats[self.key] = self.think()
        
    
    def think(self):
        return self.value