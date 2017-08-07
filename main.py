# Main file
# Created by: Sean Lim
#

from Constants import *
from Classes import BikeManager

# Bike manager instance
bike_manager = BikeManager(None)

# Enable for Debug mode
DEBUG = False

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
    bikList = getDataFrom(input('Enter the name of the bike data file: '))

    # Get data from ride history file to make sure
    # Else throw FileNotFoundError
    print("Found %i bicycle records in file." % len(bikList))

    # Move data into bike instance
    bike_manager = BikeManager(bikList)

    finished()

# Display bicycle objects currenlty in bike manager instance
def main_display_bikes():
    global bike_manager
    # Print bicycle table header
    print(DISP_BIKE_INFO_HEAD)

    # Print table
    print('\n'.join(list(map(lambda i: FORMAT_main_display_table(i), bike_manager.get_bikes()))))

    finished()

# Display bicycle detailed information
def main_display_bike_info():
    global bike_manager

    # Display bike info!
    get_bike = bike_manager.get_bikes_with_id(input('id: ').upper())

    if get_bike:
        print(DISP_BIKE_RIDE_INFO_HEAD)

        for i in get_bike.get_ride_history():
            print(FORMAT_ride_history_table(i))
        finished()

    else:
        raise Exception(ERROR_invalid("bike No. - Bike does not exist."), 3)

# Add a new bicycle
def main_add_bike():
    global bike_manager

    new_bikeID = input('Enter new Bike No.: ').upper()

    new_bike_purchaseDate = input('Purchase Date: ')

    if len(new_bikeID) != 4:
        raise Exception(ERROR_invalid("Bike No."),4)

    if len(new_bike_purchaseDate.split('/')) != 3 and len(new_bike_purchaseDate) != 10:
        raise Exception(ERROR_invalid("Date"), 4)

    bike_manager.add_bike_with_id(new_bikeID,new_bike_purchaseDate)

    print('Bicycle(%s) has been created.' % new_bikeID)

    finished()

# Perform maintenance on a bicycle.
def main_perform_maintainance():
    global bike_manager

    while True:
        print(MANTAIN_BIKE_HEADER)
        for i in bike_manager.bikes_to_service():
            print (FORMAT_maintenance_table(i))

        print('Input "exit" and press Enter to exit maintenance mode.')
        user_input = input('Bike No.:')
        if user_input == 'exit':
            finished()
            break

        else:
            bike_manager.mantain_bike(user_input)
            print('\n')


# Ride bicycles
def main_ride_bike():
    global bike_manager

    # Print all the bikes that are rideable
    print(RIDE_BIKE_HEADER)
    print('\n'.join(list(map(lambda i: FORMAT_ride_bike(i), bike_manager.get_bikes_ride()))))

    # Get bicycle object after riding
    bike_manager.ride_bike(input('Bike No.: '))

    finished()


### init Router ###
def init(withOption):
    # Get user input and route to methods
    try:
        # Get user input if router argument passed is -1 else override to specified subroutine
        userOption = get_user_input() if withOption == -1 else withOption

        display_OptionPickedMessage(userOption,OPTION_MSG[userOption])

        if userOption == 1:
            main_read_csv()

        elif userOption == 0:
            quit()

        elif bike_manager.bicycles == None:
            # No bicycle data loaded, throws exception
            raise Exception(ERROR_no_data, 1)

        elif userOption == 2:
            main_display_bikes()

        elif userOption == 3:
            main_display_bike_info()

        elif userOption == 4:
            main_add_bike()

        elif userOption == 5:
            main_perform_maintainance()

        elif userOption == 6:
            main_ride_bike()

    # Error handling Fallbacks
    except (ValueError, KeyError) as err:
        print(err if DEBUG else '\n# ERROR: {}\n' % ERROR_invalid_input)
        finished()
    except (FileNotFoundError,IsADirectoryError) as err:
        print(err if DEBUG else '\n# ERROR: %s\n' % err.args[1])
        finished()

    except Exception as error:
        if DEBUG:
            print(error)

        else:
            err_message, traceback = error.args
            print('\n# ERROR: %s\n' % err_message)

            # Route to init function with traceback
            init(-1 if input('Continue to %s? (Y/N)   ' % OPTION_MSG[traceback] ).upper() == 'N' else traceback)

if __name__ == '__main__':
    if DEBUG:
        print('\n****DEBUG MODE ON****')

    init(-1)
