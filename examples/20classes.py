from apu import *

sensor.set_vflip(0)
sensor.set_hmirror(0)


classes = ['飞机', '自行车', '鸟', '船', '瓶子', '大巴', '小车', '猫', '椅子', '牛',
           '餐桌', '狗', '马', '摩托车', '人', '植物', '羊', '沙发', '火车', '监视器']
kpu.load("/sd/20class.kmodel")
anchor = (1.08, 1.19, 3.42, 4.41, 6.63, 11.38, 9.42, 5.11, 16.62, 10.52)
kpu.init_yolo2(0.5, 0.3, 5, anchor)

while True:
    img = sensor.snapshot()
    code = kpu.run_yolo2(img)
    if code:
        for i in code:
            print('识别到{}, 位置({},{},{},{}), 概率为{:0.2f}' .format(
                classes[i['classid']], i['x'], i['y'], i['w'], i['h'], i['value']))
            img.rect(i['x'], i['y'], i['w'], i['h'])
            img.DispChar('{},概率{:0.1f}' .format(
                classes[i['classid']], i['value']), i['x'], i['y'])

    lcd.display(img)
