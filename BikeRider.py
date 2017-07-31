# Bike rider
# Created by: Sean Lim
#

from Classes import *

class BikeRider:
    def __init__(self,bike_to_ride):
        # initialise bicyle object and bike manager instance
        self.distance = 0
        self.ride_duration = 0
        self.bike_in_use = bike_to_ride
        self.battery = int(bike_to_ride.batteryPercentage)
        self.temp_to_charge = SENSE_get_current_temp() + 0.5

        # Sensehat LED debugging - disp_percent returns array of RGB tuples
        self.emulator = SenseHAT_EMULATOR(SENSE_disp_percent(bike_to_ride.batteryPercentage))

    def start_ride(self):
        movement_temp_ = (0,0,0)

        def time_instance (_time):
            self.ride_duration = _time

            if self.ride_duration < 15:
                did_move = SENSE_has_cumulative_movement(movement_temp_)
                movement_temp_ = did_move[1]

                if did_move[0] and SENSE_get_current_temp() > self.temp_to_charge:
                    # Bike moved
                    self.battery += 1
                    self.distance += 0.01

                else:
                    # Bike not moved
                    self.battery += -1

                # Update SenseHat Display
                SENSE_disp_percent(self.battery)

                # Tail recursion for time interval
                time.sleep(3)
                _time += 3
                time_instance(_time)

            else:
                # Update bike info
                self.bike_in_use.batteryPercentage = self.battery
                self.bike_in_use.kmSinceLast = str(int(self.bike_in_use.kmSinceLast) + self.distance)

                return

        # Begin Time Instance
        return time_instance(0)

    # Returns ride information in a tuple
    def dump_ride_info(self):
        return (self.bike_in_use.bikeNumber, self.ride_duration, self.distance, self.battery)
