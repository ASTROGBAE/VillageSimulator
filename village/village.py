from datetime import timedelta
import ticket as tic
from temporal import Temporal

class Village(Temporal):
    
    # name of town and starting date
    def __init__(self, name, date):
        # check obj types
        stats = {"name": name,
        "start_date": date, "current_date": 0, "food": 10, "population": 5, "weather": 25,
        "plot_farm":2, "plot_house":1}
        self.villageTicket = tic.Ticket(stats)
        super().__init__(date)
    
    # get village statistics as a ticket from ticket param
    def getVillageTicket(self, _ticket):
        if isinstance(_ticket, tic.Ticket):
            valueList = tic.Ticket(_ticket.keyList)
            return valueList.setDict(self.villageTicket)

    # add village statistic from ticket
    def addVillageTicket(self, _ticket):
        if isinstance(_ticket, tic.Ticket):
            self.villageTicket.addTicket(_ticket)
    
    # set village statistic from ticket
    def setVillageTicket(self, _ticket):
        if isinstance(_ticket, tic.Ticket):
            self.villageTicket.setFromTicket(_ticket)