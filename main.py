#
# Created by: Sean Lim
#

from constants import *

### Variables ###

bikes = Bikes([])

### Helper Methods ###

# throw error and restart process
def throws_Error(msg):
    print(f'\nERROR: {msg}\n\n')
    time.sleep(1)
    init(0)

def getUserInput():
    try:
        return int(input(MAIN_MENU))
    except ValueError:
        throws_Error("Please Enter a valid input...")

### Main scheme ###
def init(withOption):
    global bikes
    userOption = getUserInput() if withOption == 0 else withOption
    if userOption == 1:
        display_OptionPickedMessage(userOption,OPTION_MSG[userOption])
        try:
            # Read CSV File!
            bikList = getDataFrom(input('Enter the name of the data file: '))
            print(f"Found {len(bikList) } bicycle records in file")
            # Move data into bike instance
            bikes = Bikes([Bicycle(*i[:-1].split(',')) for i in bikList])
            init(0)
        except FileNotFoundError:
            throws_Error('file does not exist or is in wrong directory')
    elif userOption == 2:
        print(DISP_BIKE_INFO_HEAD)
        for i in bikes.bicycles:
            print(f'{i.bikeNumber:<4}')
init(0)
