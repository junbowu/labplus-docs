from mpython import *
import smartcamera


ai_camera = smartcamera.SmartCamera(Pin.P13, Pin.P14)
# ai_camera.repl.debug =1

ai_camera.sensor.set_windowing((224, 224))
ai_camera.sensor.run(1)

ai_camera.lcd.clear()
ai_camera.lcd.draw_string(0, 0, "MobileNet_Classifier Demo")

labels=["daisy","dandelion","roses","sunflowers","tulipss"]

task = ai_camera.kpu.load("/sd/Classifier_flower.kmodel") 
ai_camera.lcd.clear()

while True:
    img = ai_camera.sensor.snapshot()
    classifier_ret = ai_camera.kpu.forward(task, img)
    classifier_max_pro = max(classifier_ret)
    max_index = classifier_ret.index(classifier_max_pro)
    ai_camera.lcd.display(img)
    ai_camera.lcd.draw_string(0,0,"%.1f: %s" %(classifier_max_pro, labels[max_index]))
    print("类别: {}, 概率: {}" .format(labels[max_index], classifier_max_pro))
