#
# Created by: Sean Lim
#

from constants import *

### Variables ###

bikes = False

### Helper Methods ###

# throw error and restart process
def throws_Error(msg, state):
    print(f'\nERROR: {msg}\n\n')
    time.sleep(1)
    init(state)

def getUserInput():
    try:
        return int(input(MAIN_MENU))
    except ValueError:
        throws_Error("Please Enter a valid input...",0)

### Main scheme ###
def init(withOption):
    global bikes
    # Get user input
    userOption = getUserInput() if withOption == 0 else withOption
    display_OptionPickedMessage(userOption,OPTION_MSG[userOption])
    if userOption == 1:
        try:
            # Read CSV File!
            bikList = getDataFrom(input('Enter the name of the data file: '))
            print(f"Found {len(bikList) } bicycle records in file")
            # Move data into bike instance
            bikes = Bikes([Bicycle(*i[:-1].split(',')) for i in bikList])
            init(0)
        except FileNotFoundError:
            throws_Error('file does not exist or is in wrong directory',1)
    elif userOption == 2:
        if bikes:
            # Display bicycle information
            print(DISP_BIKE_INFO_HEAD)
            for i in bikes.bicycles:
                print(f' {i.bikeNumber:<9}{i.purchaseDate:<15}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<15}{i.needsService:<8}')
            print('\n')
            init(0)
        else:
            throws_Error('No data - routing to option 1 to load data first!',1)
    elif userOption == 3:
        if bikes:
            # Display bike info!
            try:
                rideHistory = bikes.get_bikes_with_id(input('id: ').upper()).rideHistory
                print(DISP_BIKE_RIDE_INFO_HEAD)
                for i in rideHistory:
                    print(f' {i[0]:<9}{i[1]+"sec":<15}{i[2]+"km":<14}{i[3]}')
            except Exception:
                throws_Error("Please Enter a valid input...",0)
        else:
            throws_Error('No data - routing to option 1 to load data first!',1)
        pass
init(0)
