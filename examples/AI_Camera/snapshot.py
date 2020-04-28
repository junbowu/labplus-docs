from mpython import *
from smartcamera import SmartCamera


ai_camera =SmartCamera(Pin.P13,Pin.P14)

LED_iS_ON = False
while True:
    if ai_camera.button.is_pressed() and LED_iS_ON== False:
        ai_camera.light.on()
        LED_iS_ON = True
        print('Light on!')
    elif  ai_camera.button.is_pressed() and LED_iS_ON== True:
        ai_camera.light.off()
        LED_iS_ON = False
        print('Light off!')
    ai_camera.lcd.display(ai_camera.sensor.snapshot())
