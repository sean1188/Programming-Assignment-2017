# SenseHat interface
# Created by: Sean Lim
#

#from sense_hat import SenseHat

#sense = SenseHat()

white = (50,255,50)
yellow = (255,50,0)
blank = (0,0,0)

# Display battery percentage on SenseHat LED
def SENSE_disp_percent (percent):
    pixel_batt_level = int(float(percent)//2 )

    disp_arr = [white for i in range(int(pixel_batt_level))]

    # Chnage color if odd number
    disp_arr.append(yellow if int(percent) % 2 != 0 else blank)

    disp_arr += [blank for i in range(int(63 - pixel_batt_level))]

    sense.set_pixels(disp_arr)

    # for debugging
    return

# Get temperature readings
def SENSE_get_current_temp():
    return sense.get_temperature()

# Function to compute culmulative movement, where stats is a tuple (pitch,roll,yaw)
def SENSE_has_cumulative_movement(stats):
    movement_info =  list(sense.get_orientation_degrees().values())
    # Return movement and update vectors
    return True if sum(map(lambda x,y: abs(x - y),movement_info,stats)) > 20 else False, movement_info
