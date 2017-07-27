# Classes, managers and factory methods
# Created by: Sean Lim
#

from Constants import *

### Bicycle class ###
class Bicycle:
    def __init__ (self,bikeNumber, purchaseDate, batteryPercentage, lastMaintenance , kmSinceLast):
        self.bikeNumber = bikeNumber
        self.purchaseDate = purchaseDate
        self.batteryPercentage = batteryPercentage
        self.lastMaintenance = lastMaintenance
        self.kmSinceLast = kmSinceLast

        # Tuple containing boolean for service requirements with format - (Months, km, Batt)
        service_information = ((dateObjectFrom(time.strftime("%d/%m/%Y")) - dateObjectFrom(lastMaintenance)).days > (365/2), float(kmSinceLast) >50 , float(batteryPercentage) < 10)
        # Binary value for servicing
        self.needsService = "Y" if True in service_information else "N"
        # String describing service information
        self.service_information_string = " & ".join(list(map(lambda x: x[1] ,filter(lambda x: x[0] ,zip(service_information,("Months","km","batt"))))))
        # List of ride history information
        self.rideHistory = [i[:-1].split(',') for i in open('./data/Assignment_Data2.csv','r') if i.split(',')[0] == bikeNumber]

### Bicycle manager ###
class BikeManager:

    # Factory method
    def __init__ (self,bicycles):
        self.bicycles = list(map(lambda i: Bicycle(*i[:-1].split(',')), bicycles)) if bicycles != None else None

    def add_bike_with_id(self,bikeNumber,dateCreated):
        if self.get_bikes_with_id(bikeNumber) == False:
            self.bicycles.append(Bicycle(bikeNumber,dateCreated,'100',time.strftime("%d/%m/%Y"),'0.00'))
        else:
            raise Exception(f'Bike ({bikeNumber}) already exists', 4)

    # Returns an iterable
    def get_bikes (self):
        return iter(self.bicycles)

    # Returns list of Bikes that need to be serviced
    def bikes_to_service(self):
        return list(filter(lambda x: x.needsService == "Y", self.bicycles))

    # Mantains bike
    def mantain_bike(self, bike_number):
        bike_to_service = self.get_bikes_with_id(bike_number)
        # Ensure that bike to service exists before mutating attributes
        if (bike_to_service in self.bikes_to_service()):
            self.bicycles[self.bicycles.index(bike_to_service)] = Bicycle(bike_to_service.bikeNumber,bike_to_service.purchaseDate,"100",time.strftime("%d/%m/%Y"),"0.00")
            print(f'Successfully serviced bicycle {bike_to_service.bikeNumber}')

        elif bike_to_service == False:
            raise Exception('Bicycle does not exist',5)

        elif bike_to_service not in self.bikes_to_service():
            raise Exception('Bicycle is not due for service',5)

    def get_bikes_with_id(self,bikeNumber):
        fil = list(filter(lambda x: x.bikeNumber == bikeNumber, self.bicycles))
        return fil[0] if len(fil) > 0 else False
