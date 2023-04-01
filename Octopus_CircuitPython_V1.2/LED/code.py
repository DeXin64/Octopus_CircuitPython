import time
form LED import *


led = LED(board.GP26)

led.set_led(1)
time.sleep(1)
led.set_led_bright(0)
time.sleep(1)
