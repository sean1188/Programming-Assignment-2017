# Classes, managers and factory methods
# Created by: Sean Lim
#

from Constants import *
from SenseHatManager import *

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
        self.rideHistory = [i[:-1].split(',') for i in getDataFrom('data2.csv') if i.split(',')[0] == bikeNumber]

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

    # Returns an iterable of all bikes
    def get_bikes (self):
        return iter(self.bicycles)

    # Return iterable of rideable bikes
    def get_bikes_ride (self):
        return iter(list(filter(lambda x: x.needsService == "N", self.bicycles)))

    # Ride a bicycle
    def ride_bike (self,bike_number):
        if (bike_number in [i.bikeNumber for i in self.get_bikes_ride()]):
            # Starts a new bike ride
            print(f'{BICYCLE}\nRiding Bike No. {bike_number} ...')
            # Creates a new instance of BikeRider that passes bicyle object and an instance of BikeManager
            bike_ride = BikeRider(self.get_bikes_with_id(bike_number), self)
            return bike_ride.start_ride()
        else:
            # Bike either does not exist or need service
            raise Exception(ERROR_Bike_not_due(bike_number, 'due for service')if self.get_bikes_with_id(bike_number) else ERROR_Bike_no_exist, 6)

    # Returns list of Bikes that need to be serviced
    def bikes_to_service(self):
        return list(filter(lambda x: x.needsService == "Y", self.bicycles))

    # Services bike
    def mantain_bike(self, bike_number):
        bike_to_service = self.get_bikes_with_id(bike_number)
        # Ensure that bike to service exists before mutating attributes
        if (bike_to_service in self.bikes_to_service()):
            self.bicycles[self.bicycles.index(bike_to_service)] = Bicycle(bike_to_service.bikeNumber,bike_to_service.purchaseDate,"100",time.strftime("%d/%m/%Y"),"0.00")
            print(f'Successfully serviced bicycle {bike_to_service.bikeNumber}')

        elif bike_to_service == False:
            raise Exception(ERROR_Bike_no_exist(bike_number),5)

        elif bike_to_service not in self.bikes_to_service():
            raise Exception(ERROR_Bike_not_due(bike_number,'due for service'),5)

    def get_bikes_with_id(self,bikeNumber):
        fil = list(filter(lambda x: x.bikeNumber == bikeNumber, self.bicycles))
        return fil[0] if len(fil) > 0 else False

# Bike rider
class BikeRider:
    def __init__(self,bike_to_ride, bike_manager_instance):
        # initialise bicyle object and bike manager instance
        self.distance = 0
        self.ride_duration = 0
        self.battery = int(bike_to_ride.batteryPercentage)
        self.bike_in_use = bike_to_ride
        self.bike_manager_instance = bike_manager_instance
        # Sensehat LED debugging - disp_percent returns array of RGB tuples
        self.emulator = SenseHAT_EMULATOR(disp_percent(bike_to_ride.batteryPercentage))

    def start_ride(self):
        # Recursive 3 second time instance
        def time_instance (_time):
            self.battery += -1
            self.emulator.update_grid(disp_percent(self.battery))
            time.sleep(3)
            _time += 3
            time_instance(_time)
        # Begin Time Instance
        time_instance(0)
