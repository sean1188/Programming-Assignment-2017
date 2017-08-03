# SenseHat interface
# Created by: Sean Lim
#

# from sense_hat import SenseHat, ACTION_PRESSED
#
# sense = SenseHat()

white = (255,255,255)
yellow = (255,255,0)
blank = (0,0,0)

# Display battery percentage on SenseHat LED
def SENSE_disp_percent (percent):
    pixel_batt_level = int(float(percent)//2 )

    disp_arr = [white for i in range(int(pixel_batt_level))]

    # Chnage color if odd number
    disp_arr.append(yellow if int(percent) % 2 != 0 else blank)

    disp_arr += [blank for i in range(int(63 - pixel_batt_level))]
    # sense.set_pixels(disp_arr)

    # for debugging
    return disp_arr

# Get temperature readings
def SENSE_get_current_temp():
    return sense.get_temperature()

# Function to compute culmulative movement, where stats is a tuple (pitch,roll,yaw)
def SENSE_has_cumulative_movement(stats):
    movement_info =  list(sense.get_orientation_degrees().values())

    # Return movement and update vectors
    return True if sum(map(lambda x,y: abs(x - y),movement_info),stats) > 20 else False, movement_info

# SenseHat LED grid emulator purely for debugging purposes lol
class SenseHAT_EMULATOR:

    LED_map = {
        (255,255,255) : '=',
        (255,255,0) : '-',
        (0,0,0) : '0'
    }

    def __init__(self,display_array):
        print('SENSEHAT EMULATOR START')

        self.update_grid(display_array)

    def update_grid(self,display_array):
        self.LED_grid = list(map(lambda x: self.LED_map[x],display_array))

        print("\n\n")
        for i in enumerate(self.LED_grid):
            print('{:<6}'.format(i[1]) if i[0] % 8 != 0 else '\n\n{:<6}'.format(i[1]) , end= "")
        print('\n\n')
