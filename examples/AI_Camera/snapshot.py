from mpython import *
import smartcamera
import time
import music
ai_camera = smartcamera.SmartCamera(Pin.P13, Pin.P14)

while True:
    img = ai_camera.sensor.snapshot()
    ai_camera.lcd.display(img)
    if ai_camera.button.was_pressed():
        localtime = time.localtime()
        img_name = "img_{:2d}_{:2d}_{:2d}.jpg" .format(
            localtime[3], localtime[4], localtime[5])
        img.save("/sd/{}" .format(img_name))
        music.pitch(1000, 200)
        print('Save image: {}' .format(img_name))
