# Constant variables, helpers and helper methods
# Created by: Sean Lim
#

import time
import datetime

### Constant variables ###

MAIN_MENU = """\

ADMIN MENU
==========
[1] Read bicycle info from file
[2] Display all bicycle info with servicing indication
[3] Display selected bicycle info
[4] Add a bicycle
[5] Perform bicycle maintenance

RIDER MENU
==========
[6]  Ride a bicycle

[0]  Exit
Enter your option: \
"""
DISP_BIKE_INFO_HEAD = """
 Bike No. Purchase Date  Batt % Last Maintenance KM Since Last  Service?
 -------- -------------  ------ ---------------- -------------  --------
"""
ERROR = "Invalid Input!"
OPTION_MSG = {
              1 : 'Read bicycle info from file',
              2 : 'Display all bicycle info with servicing indication',
              3 : 'Display selected bicycle info'
              }

### Helper methods ###

def display_OptionPickedMessage(option, instructions):
    print(f'\nOption {option}: {instructions}')

getDataFrom = lambda fileName:[i for i in open(f'./data/{fileName}',"r")][1:]
dateObjectFrom = lambda dateStr : datetime.date(*map(int,reversed(dateStr.split('/'))))

### Bicycle DOM ###
class Bicycle:
    def __init__ (self,bikeNumber, purchaseDate, batteryPercentage, lastMaintenance , kmSinceLast):
        self.bikeNumber = bikeNumber
        self.purchaseDate = purchaseDate
        self.batteryPercentage = batteryPercentage
        self.lastMaintenance = lastMaintenance
        self.kmSinceLast = kmSinceLast
        self.needsService = "Y" if (dateObjectFrom(time.strftime("%d/%m/%Y")) - dateObjectFrom(lastMaintenance)).days > (365/2) or float(kmSinceLast) >50 or float(batteryPercentage) < 10 else "N"

### Bike operations helper class ###
class Bikes:
    def __init__ (self,bicycles):
        # Bikes is an array of bicycles
        self.bicycles = bicycles

    def getBikes_With_id(self,bikeNumber):
        fil = list(filter(lambda x: x.bikeNumber == bikeNumber, self.bikes))
        return fil[0] if len(fil) > 0 else False

    def addBike_With_id(self,bikeNumber,dateCreated):
        if getBikes_With_id(bikeNumber) == False:
            self.bicycles.append(Bicycle(bikeNumber,dateCreated))
        else:
            print('Bike addition failed, bike with same number already exists!')
