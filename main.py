#
# Created by: Sean Lim
#

from Constants import *
from Classes import Bicycle, BikeManager

### Variables ###

bike_manager = BikeManager(None)

# Debug mode
DEBUG = True

### Helper Methods ###

# Display main menu and return user's selection
def get_user_input():
    return int(input(MAIN_MENU))

# Finished task
def finished():
    input("\nPress Enter to Continue...")
    init(-1)

# Read CSV file
def main_read_csv():
    global bike_manager
    # Read CSV File!
    bikList = getDataFrom(input('Enter the name of the data file: '))
    print(f"Found {len(bikList) } bicycle records in file.")
    # Move data into bike instance
    bike_manager = BikeManager([Bicycle(*i[:-1].split(',')) for i in bikList])
    finished()

# Display bicycle objects currenlty in bike manager instance
def main_display_bikes():
    global bike_manager
    # Check if instance of bike manager is valid
    if bike_manager.bicycles == None:
        raise Exception(ERROR_no_data, 1)
    else:
        # Display bicycle information
        print(DISP_BIKE_INFO_HEAD)
        for i in bike_manager.get_bikes():
            print(f'{i.bikeNumber:<9}{i.purchaseDate:<15}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<15}{i.needsService:<8}')
        finished()

def main_display_bike_info():
    global bike_manager
    if bike_manager.bicycles == None:
        raise Exception(ERROR_no_data,1)
    else:
        # Display bike info!
        rideHistory = bike_manager.get_bikes_with_id(input('id: ').upper()).rideHistory
        print(DISP_BIKE_RIDE_INFO_HEAD)
        for i in rideHistory:
            print(f'{i[0]:<9}{i[1]+"sec":<15}{i[2]+"km":<14}{i[3]}')
        finished()

def main_add_bike():
    global bike_manager
    new_bikeID = input('Enter new Bike No.: ')
    new_bike_purchaseDate = input('Purchase Date: ')
    if len(new_bikeID) != 4:
        raise Exception(ERROR_invalid("Bike No."),4)
    if len(new_bike_purchaseDate.split('/')) != 3 and len(new_bike_purchaseDate) != 10:
        raise Exception(ERROR_invalid("Date"), 4)
    bike_manager.add_bike_with_id(new_bikeID,new_bike_purchaseDate)
    print(f'Bicycle({new_bikeID}) has been created.')
    finished()

def main_perform_maintainance():
    global bike_manager
    print(MANTAIN_BIKE_HEADER)
    for i in bike_manager.bikes_to_service():
        service_info_string = " & ".join(list(map(lambda x: x[1] ,filter(lambda x: x[0] ,zip(i.service_information,("Months","km","batt"))))))
        print (f'{i.bikeNumber:<9}{i.batteryPercentage:<7}{i.lastMaintenance:<17}{i.kmSinceLast:<14}{service_info_string:<9}')
    print('Input "exit" and press Enter to exit maintenance mode.')
    while True:
        user_input = input('Bike No.: ')
        if user_input == 'exit':
            finished()
            break
        else:
            bike_manager.mantain_bike(user_input)
            finished()
            break

# init Router
def init(withOption):
    # Get user input and route to methods
    try:
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
            quit()
    except (ValueError, KeyError) as err:
        print(err if DEBUG else f'\n# ERROR: Please enter a valid input...\n')
        finished()
    except FileNotFoundError as err:
        print(err if DEBUG else f'\n# ERROR: {err.args[1]}\n')
        finished()
    except Exception as error:
        err_message, traceback = error.args
        print(err if DEBUG else f'\n# ERROR: {err_message}\n')
        init(-1 if input(f'Continue to {OPTION_MSG[traceback]}? (Y/N)   ').upper() == 'N'else traceback)

init(-1)
