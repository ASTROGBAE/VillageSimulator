from event import Event

class Weather(Event):
    def __init__(self, date):
        super().__init__(["weather"], date) # define keys and starting date
        
     # process done during each iteration, make sure to copy this to each new Event class
     # TODO make more complicated!
     # represents degrees celcius 
    def think(self, newDate):
        value = 25
        return value # returns (key, value)