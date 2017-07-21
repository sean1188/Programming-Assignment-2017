#
# Created by: Sean Lim
#

from Constants import *
from Classes import Bicycle, BikeManager

### Variables ###

bike_manager = BikeManager

### Helper Methods ###

# throw error and restart process
def throws_Error(msg, state):
    print(f'\nERROR: {msg}\n\n')
    time.sleep(1)
    init(state)

def get_user_input():
    try:
        return int(input(MAIN_MENU))
    except ValueError:
        throws_Error("Please Enter a valid input...",-1)

### Main scheme ###
# Main methods
def main_read_csv():
    global bike_manager
    try:
        # Read CSV File!
        bikList = getDataFrom(input('Enter the name of the data file: '))
        print(f"Found {len(bikList) } bicycle records in file")
        # Move data into bike instance
        bike_manager = BikeManager([Bicycle(*i[:-1].split(',')) for i in bikList])
        init(-1)
    except FileNotFoundError:
        throws_Error('file does not exist or is in wrong directory',1)

def main_display_bikes():
    global bike_manager
    if bike_manager:
        # Display bicycle information
        print(DISP_BIKE_INFO_HEAD)
        for i in bike_manager.bicycles:
            print(f' {i.bikeNumber:<9}{i.purchaseDate:<15}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<15}{i.needsService:<8}')
        print('\n')
        init(-1)
    else:
        throws_Error('No data - routing to option 1 to load data first!',1)

def main_display_bike_info():
    global bike_manager
    if bike_manager:
        # Display bike info!
        try:
            rideHistory = bike_manager.get_bikes_with_id(input('id: ').upper()).rideHistory
            print(DISP_BIKE_RIDE_INFO_HEAD)
            for i in rideHistory:
                print(f' {i[0]:<9}{i[1]+"sec":<15}{i[2]+"km":<14}{i[3]}')
            init(-1)
        except Exception:
            throws_Error("Please Enter a valid input...",3)
    else:
        throws_Error('No data - routing to option 1 to load data first!',1)

def main_add_bike():
    global bike_manager
    try:
        new_bikeID = input('Enter new Bike No.: ')
        if len(new_bikeID) != 4:
            raise Exception
        new_bike_purchaseDate = input('Purchase Date: ')
        if len(new_bike_purchaseDate.split('/')) != 3 and len(new_bike_purchaseDate) != 10:
            raise Exception
        bike_manager.add_bike_with_id(new_bikeID,new_bike_purchaseDate)
        print(f'Bicycle({new_bikeID}) has been created.')
        init(-1)
    except Exception:
        throws_Error('Invalid input(s)', 4)

def main_perform_maintainance():
    global bike_manager
    print(MANTAIN_BIKE_HEADER)
    for i in bike_manager.get_bikes_toService():
        service_info_string = " & ".join(list(map(lambda x: x[1] ,filter(lambda x: x[0] ,zip(i.service_information,("Months","km","batt"))))))
        print (f' {i.bikeNumber:<9}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<14}{service_info_string:<9}')


# init Router
def init(withOption):
    # Get user input and route to methods
    userOption = get_user_input() if withOption == -1 else withOption
    display_OptionPickedMessage(userOption,OPTION_MSG[userOption])
    if userOption == 1:
        main_read_csv()
    elif userOption == 2:
        main_display_bikes()
    elif userOption == 3:
        main_display_bike_info()
    elif userOption == 4:
        main_add_bike()
    elif userOption == 5:
        main_perform_maintainance()
    elif userOption == 0:
        sys.exit()
init(-1)
