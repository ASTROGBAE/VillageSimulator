class Ticket():
    """start param can be list of strings OR a dictoionary containing values
    """
    def __init__(self, _startParam):
        self.keyList = [] # TODO class encapsulation on keyList?
        self.statDict = {}
        if isinstance(_startParam, list):
            self.keyList = _startParam
            self.resetDeltaDict()
        elif isinstance(_startParam, dict):
            for key, val in _startParam.items():
                self.keyList += key
                self.statDict[key] = val
    
    def resetDeltaDict(self): # TODO is this reset necessary? Just make a new ticket!
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
            
    def addTicket(self, _ticket):
        for key, val in _ticket.statDict.items():
            if key in self.keyList:
                self.addValue(key, val)
                
    def setFromTicket(self, _ticket):
        for key, val in _ticket.statDict.items():
            if key in self.keyList:
                self.setValue(key, val)
            