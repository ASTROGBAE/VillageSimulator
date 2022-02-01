class Ticket():
    """start param can be list of strings OR a dictoionary containing values
    """
    def __init__(self, _startParam):
        # TODO scope keyList so we don't need it, make it so we can just get keys from dict, don't need a list...
        self.keyList = [] # TODO class encapsulation on keyList?
        self.statDict = {}
        if isinstance(_startParam, list) and isinstance(_startParam[0], str): # if list of strings (keyList), simply add and set all values to 0
            # TODO make this stype-checking better? Check if all entries are strings...
            self.keyList = _startParam
            for key in self.keyList: self.statDict[key] = 0
        elif isinstance(_startParam, dict):
            for key, val in _startParam.items():
                self.keyList += key
                self.statDict[key] = val
        elif isinstance(_startParam, list) and len(_startParam) == 2 and isinstance(_startParam[0], list) and isinstance(_startParam[1], list): # if of format [keyList][valPerKey]
            for key in _startParam[0]:
                for val in _startParam[1]: # add in key,val as per above format: [keyList][val]
                    self.keyList += [key]
                    self.statDict[key] = val
        #else:
            # TODO invalid start param?
        
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
            