import lcdi2c
from time import *

mylcd = lcdi2c.lcd()

mylcd.lcd_display_string("Hello World!", 1)