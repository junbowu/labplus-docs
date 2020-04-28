from apu import *

sensor.set_vflip(0)
sensor.set_hmirror(0)

while True:
    lcd.display(sensor.snapshot())
