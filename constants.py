# Constant variables, helpers and helper methods
# Created by: Sean Lim
#

import time
import datetime
import sys

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
DISP_BIKE_RIDE_INFO_HEAD = """
 Bike No. Ride duration  Ride distance Battery %
 -------- -------------  ------------- ---------
"""
ERROR = "Invalid Input!"
OPTION_MSG = {
              0 : ' EXIT - Bye bye!',
              1 : 'Read bicycle info from file',
              2 : 'Display all bicycle info with servicing indication',
              3 : 'Display selected bicycle info',
              4 : 'Add a bicycle.'
              }

### Helper methods ###
def display_OptionPickedMessage(option, instructions):
    print(f'\nOption {option}: {instructions}')

getDataFrom = lambda fileName:[i for i in open(f'./data/{fileName}',"r")][1:]

dateObjectFrom = lambda dateStr : datetime.date(*map(int,reversed(dateStr.split('/'))))
