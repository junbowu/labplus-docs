from mpython import *
import smartcamera


ai_camera = smartcamera.SmartCamera(Pin.P13, Pin.P14)

classes = ['飞机', '自行车', '鸟', '船', '瓶子', '大巴', '小车', '猫', '椅子', '牛',
           '餐桌', '狗', '马', '摩托车', '人', '植物', '羊', '沙发', '火车', '监视器']
task = ai_camera.kpu.load(0x640000)   # 20类模型的flash地址
anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
ai_camera.kpu.init_yolo2(task, 0.5, 0.3, 5, anchor)

while True:
    img = ai_camera.sensor.snapshot()
    code = ai_camera.kpu.run_yolo2(task, img)
    if code:
        for i in code:
            print('识别到{}, 位置({},{},{},{}), 概率为{:0.2f}' .format(
                classes[i['classid']], i['x'], i['y'], i['w'], i['h'], i['value']))
            img.rect(i['x'], i['y'], i['w'], i['h'])
            img.DispChar('{},概率{:0.1f}' .format(
                classes[i['classid']], i['value']), i['x'], i['y'])

    ai_camera.lcd.display(img)
