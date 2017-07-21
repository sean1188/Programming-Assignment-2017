from Constants import *

### Bicycle DOM ###
class Bicycle:
    def __init__ (self,bikeNumber, purchaseDate, batteryPercentage, lastMaintenance , kmSinceLast):
        self.bikeNumber = bikeNumber
        self.purchaseDate = purchaseDate
        self.batteryPercentage = batteryPercentage
        self.lastMaintenance = lastMaintenance
        self.kmSinceLast = kmSinceLast
        # Tuple containing boolean for service requirements
        # Service tuple format - (Months, km, Batt)
        self.service_information = ((dateObjectFrom(time.strftime("%d/%m/%Y")) - dateObjectFrom(lastMaintenance)).days > (365/2), float(kmSinceLast) >50 , float(batteryPercentage) < 10)
        self.needsService = "Y" if True in self.service_information else "N"
        # List of ride history information
        self.rideHistory = [i[:-1].split(',') for i in open('./data/Assignment_Data2.csv','r') if i.split(',')[0] == bikeNumber]

class BikeManager:
    def __init__ (self,bicycles):
        self.bicycles = bicycles

    def get_bikes_toService(self):
        return list(filter(lambda x: x.needsService == "Y", self.bicycles))

    def mantain_bike(self, get_bike):
        self.bicycles[self.bicycles.index(get_bike)] = Bicycle(get_bike.bikeNumber,get_bike.purchaseDate,"100",time.strftime("%d/%m/%Y"),"0.00")

    def get_bikes_with_id(self,bikeNumber):
        fil = list(filter(lambda x: x.bikeNumber == bikeNumber, self.bicycles))
        return fil[0] if len(fil) > 0 else False

    def add_bike_with_id(self,bikeNumber,dateCreated):
        if self.get_bikes_with_id(bikeNumber) == False:
            self.bicycles.append(Bicycle(bikeNumber,dateCreated,'100',time.strftime("%d/%m/%Y"),'0.00'))
            print (self.bicycles)
        else:
            raise Exception
