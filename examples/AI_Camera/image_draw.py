from mpython import *
import smartcamera
import time

ai_camera =smartcamera.SmartCamera(Pin.P13,Pin.P14)

# 图片填充红色
ai_camera.image.fill((255, 0, 0))
ai_camera.lcd.display(ai_camera.image)
time.sleep(0.4)

# 图片填充绿色
ai_camera.image.fill((0, 255, 0))
ai_camera.lcd.display(ai_camera.image)
time.sleep(0.4)

# 图片填充蓝色
ai_camera.image.fill((0, 0, 255))
ai_camera.lcd.display(ai_camera.image)
time.sleep(0.4)

# 图片像素点清除
ai_camera.image.clear()
# 字符显示
ai_camera.image.DispChar("Hello,MaixPy!", 0, 0, color=(255, 255, 255))
ai_camera.image.DispChar("你好,掌控板!", 0, 16, color=(255, 0, 0))

# 画线
ai_camera.image.DispChar("水平线", 0, 40,(255, 255, 0))
ai_camera.image.hline(40, 50, 50, c=(255, 255, 0), thickness=1)
ai_camera.image.DispChar("垂直线", 0, 50,(255,0,0))
ai_camera.image.vline(50, 60, 50, c=(255,0,0), thickness=2)
ai_camera.image.DispChar("任意线", 0, 60,(0, 255, 255))
ai_camera.image.line(50, 70, 80, 90, c=(0, 255, 255), thickness=1)


#画点
import random
ai_camera.image.DispChar('画点',100,80)
for i in range(20):
    x=random.randint(100,150)
    y=random.randint(80,130)
    ai_camera.image.pixel(x,y,c=(255,255,0))

ai_camera.lcd.display(ai_camera.image)

# # 绘制矩形框
ai_camera.image.DispChar('矩形', 100, 0)
ai_camera.image.rect(100, 16, 30, 30, c=(255, 0, 0), thickness=2)

# # 绘制实心矩形
ai_camera.image.DispChar('实心矩形', 150, 0)
ai_camera.image.fill_rect(150, 16, 30, 30, c=(0, 255, 0))


# 画中画
ai_camera.image.DispChar('画中画', 150, 60)
ai_camera.image.draw_image(ai_camera.sensor.snapshot(),150,80,x_scale=0.2, y_scale=0.2)
ai_camera.lcd.display(ai_camera.image)
