# DankBikes
Pretty c00l python bike manager thinggy
## Structure of Program

**main.py** contains the main code for the program. `init()` is called when the program first starts, and controls flow. Methods for each option exist as subroutines within main.py. `bike_manager` is an instance of `BikeManager`, and is used to store & manipulate `Bicycle` objects.

**Classes.py** is where classes `BikeManager` and `Bicycle` are defined, contains key methods and functions. Each `Bicycle` class has several dump functions in order to curry down formatting in main.py.

**constants.py** contains useful methods, variables and lambdas that can be used globally.

**BikeRider.py** is where the `BikeRider` class is defined, bike ride information is stored in each instance of `BikeRider`.

**SenseHatManager.py** contains methods to allow easy I/O to the Pi with the SenseHAT module.
