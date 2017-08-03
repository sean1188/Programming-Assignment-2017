# Classes, managers and factory methods
# Created by: Sean Lim
#

from Constants import *
from SenseHatManager import *
from BikeRider import BikeRider

#                     #
##                   ##
### Bicycle object  ###
##                   ##
#                     #
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

    # Functions to dump all bicycle information into a tuple
    def dump_main_info(self):
        return (self.bikeNumber, self.purchaseDate, self.batteryPercentage, self.lastMaintenance, self.kmSinceLast, self.needsService)
    def dump_service_info(self):
        return (self.bikeNumber, self.batteryPercentage, self.lastMaintenance, self.kmSinceLast, self.service_information_string)
    def dump_ride_info(self):
        return (self.bikeNumber, self.batteryPercentage, self.kmSinceLast)

#                     #
##                   ##
### Bicycle manager ###
##                   ##
#                     #
class BikeManager:

    def __init__ (self,bicycles):
        self.bicycles = list(map(lambda i: Bicycle(*i[:-1].split(',')), bicycles)) if bicycles != None else None

    # Adds a new bike
    def add_bike_with_id(self,bikeNumber,dateCreated):
        if self.get_bikes_with_id(bikeNumber) == False:
            self.bicycles.append(Bicycle(bikeNumber,dateCreated,'100',time.strftime("%d/%m/%Y"),'0.00'))

        else:
            raise Exception('Bike (%s) already exists' % bikeNumber, 4)

    # Returns an iterable of all bikes
    def get_bikes (self):
        return iter(self.bicycles)

    # Return iterable of bikes that are rideable
    def get_bikes_ride (self):
        return iter(list(filter(lambda x: x.needsService == "N", self.bicycles)))

    # Ride a bicycle
    def ride_bike (self,bike_number):
        if (bike_number in [i.bikeNumber for i in self.get_bikes_ride()]):
            # Starts a new bike ride
            print('%s\nRiding Bike No. %s ...' % (BICYCLE, bike_number) )

            # Passes instance of bicycle object to bike rider class
            bike_ride = BikeRider(self.get_bikes_with_id(bike_number))

            # Starts ride
            bike_ride.start_ride()

            # Continues when bike is finished riding
            # Update csv file with data from bike ride
            write_csv = open('./data/data2.csv','a')
            write_csv.write('\n' +','.join( map( str, bike_ride.dump_ride_info() ) ))
            write_csv.close()

            # Returns updated bike
            return bike_ride

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
            # Service the bike
            bike_to_service.batteryPercentage = '100'
            bike_to_service.lastMaintenance = time.strftime("%d/%m/%Y")
            bike_to_service.needsService = 'N'
            bike_to_service.kmSinceLast = '0.00'

            print('Successfully serviced bicycle %s' % bike_to_service.bikeNumber)

        elif bike_to_service == False:
            # Bike does not exist
            raise Exception(ERROR_Bike_no_exist(bike_number),5)

        elif bike_to_service not in self.bikes_to_service():
            # Bike not due for service
            raise Exception(ERROR_Bike_not_due(bike_number,'due for service'),5)

    # Get bicycle by ID
    def get_bikes_with_id(self,bikeNumber):
        fil = list(filter(lambda x: x.bikeNumber == bikeNumber, self.bicycles))
        return fil[0] if len(fil) > 0 else False
