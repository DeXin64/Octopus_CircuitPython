from OLED import *
import time


oled = OLED(board.GP17, board.GP16)


oled.set_clear()
oled.draw_rectangle(0, 0, 128, 64, 1)
oled.show()

