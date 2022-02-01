class Ticket():
    def __init__(self, _keyList):
        self.statDict = {}
        self.keyList = _keyList
        self.resetDeltaDict()
        
    
    def resetDeltaDict(self):
        """reset all values in deltaDict to 0 for next operation
        """
        for key in self.keyList: self.statDict[key] = 0 # add 
        
    def addValue(self, key, val):
        """add val to Delta TODO make this delta group its own class?

        Args:
            key ([type]): key valid in 

        Returns:
            [type]: [description]
        """
        if (key in self.keyList):
            self.statDict[key] += val # add 
            
    def setValue(self, key, val):
        """add val to Delta TODO make this delta group its own class?

        Args:
            key ([type]): key valid in 

        Returns:
            [type]: [description]
        """
        if (key in self.keyList):
            self.statDict[key] = val # set
        