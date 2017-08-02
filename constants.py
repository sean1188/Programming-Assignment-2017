# Constant variables, helpers and helper methods
# Created by: Sean Lim
#

import time
import datetime

### Constant variables ###
MAIN_MENU = """\
 _____          _   _ _  __  ____ _____ _  ________  _____
|  __ \   /\   | \ | | |/ / |  _ \_   _| |/ /  ____|/ ____|
| |  | | /  \  |  \| | ' /  | |_) || | | ' /| |__  | (___
| |  | |/ /\ \ | . ` |  <   |  _ < | | |  < |  __|  \___ \

| |__| / ____ \| |\  | . \  | |_) || |_| . \| |____ ____) |
|_____/_/    \_\_| \_|_|\_\ |____/_____|_|\_\______|_____/

======================================================
ADMIN MENU
======================================================
[1] Read bicycle info from file
[2] Display all bicycle info with servicing indication
[3] Display selected bicycle info
[4] Add a bicycle
[5] Perform bicycle maintenance

======================================================
RIDER MENU
======================================================
[6]  Ride a bicycle

Input 0 to exit

------------------------------------------------------
Enter your option: \
"""
DISP_BIKE_INFO_HEAD = """
Bike No. Purchase Date  Batt % Last Maintenance KM Since Last  Service?
-------- -------------  ------ ---------------- -------------  --------"""
DISP_BIKE_RIDE_INFO_HEAD = """
Bike No. Ride duration  Ride distance Battery %
-------- -------------  ------------- ---------"""
MANTAIN_BIKE_HEADER = """
BIKE SERVICING MODE

Bike No. Batt % Last Maintenance KM since Last Reason/s
-------- ------ ---------------- ------------- ---------"""
RIDE_BIKE_HEADER = """
Bike No. Batt % KM since Last
-------- ------ -------------"""
BICYCLE = """
 -------- __@      __@       __@       __@      __~@
 ----- _`\<,_    _`\<,_    _`\<,_     _`\<,_    _`\<,_
 ---- (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)  (*)/ (*)
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
OPTION_MSG = {
              0 : 'EXIT - Bye bye!',
              1 : 'Read bicycle info from file',
              2 : 'Display all bicycle info with servicing indication',
              3 : 'Display selected bicycle info',
              4 : 'Add a bicycle',
              5 : 'Perform bicycle maintenance',
              6 : 'Ride a bicycle'
              }

# Error messages
ERROR_no_data = "No data - enter csv file name in option 1 first!"
ERROR_invalid_input = "Please Enter a valid input..."
ERROR_Bike_no_exist = lambda x : 'Bicycle (%s) does not exist' % x
ERROR_Bike_not_due = lambda x,y  : 'Bicycle (%s) not %s' % (x,y)
ERROR_invalid = lambda x: 'Invalid %s.' % x

### Helper methods ###
def display_OptionPickedMessage(option, instructions):
    print('\nOption %i: %s' % (option,instructions))
getDataFrom = lambda fileName: [i for i in open('./data/%s' % fileName,"r")][1:]
dateObjectFrom = lambda dateStr : datetime.date(*map(int,reversed(dateStr.split('/'))))

# Table formatting
FORMAT_ride_history_table = lambda i: f'{i[0]:<9}{i[1]+"sec":<15}{i[2]+"km":<14}{i[3]}'
FORMAT_main_display_table = lambda i: '{:<9}{:<15}{:<7}{:<17}{:<15}{:<8}'.format(*i.dump_main_info())
FORMAT_maintenance_table = lambda i: '{:<9}{:<7}{:<17}{:<14}{:<9}'.format(*i.dump_service_info())
FORMAT_ride_bike = lambda i: '{:<9}{:<7}{:<13}'.format(*i.dump_ride_info())
