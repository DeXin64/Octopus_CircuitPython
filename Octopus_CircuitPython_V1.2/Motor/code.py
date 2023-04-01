from  Motor import *

FANS1 = Motor(board.GP26)

while True:
    FANS1.set_fan(20)

