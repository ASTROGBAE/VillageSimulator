import village

class Event():
    def __init__(self, value):
        self.value = value
        
    
    def think(self):
        key = "define key in specific event child class, key is for village stats"
        return (key, self.value)