from mpython import *
from smartcamera import SmartCamera


ai_camera =SmartCamera(Pin.P13,Pin.P14)

# 模型加载
ai_camera.kpu.load('/sd/facedetect.kmodel')
anchor = (1.889, 2.5245, 2.9465, 3.94056, 3.99987,
          5.3658, 5.155437, 6.92275, 6.718375, 9.01025)

ai_camera.kpu.init_yolo2(0.5, 0.3, 5, anchor)
while True:
    img = ai_camera.sensor.snapshot()
    code = ai_camera.kpu.run_yolo2(img)
    if code:
        for i in code:
            print('侦测到人脸, 位置({},{},{},{}), 概率为{:0.2f}'.format(
                i['x'], i['y'], i['w'], i['h'], i['value']))
            img.rect(i['x'], i['y'], i['w'], i['h'])
            img.DispChar('{:0.2f}' .format(i['value']), i['x'], i['y'])
    ai_camera.lcd.display(img)
