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
def disp_percent (percent):
    pixel_batt_level = int(float(percent)//2 )
    disp_arr = [white for i in range(int(pixel_batt_level))]
    # Chnage color if odd number
    disp_arr.append(yellow if int(percent) % 2 != 0 else blank)
    # sense.set_pixels(disp_arr + [blank for i in range(64 - pixel)])
    # for debugging
    return disp_arr + [blank for i in range(int(63 - pixel_batt_level))]


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
            print(f'{i[1]:<6}' if i[0] % 8 != 0 else f'\n\n{i[1]:<6}', end= "")
        print('\n\n')
