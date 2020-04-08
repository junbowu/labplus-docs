from apu import *

# 图片填充红色
img.fill((255, 0, 0))
lcd.display(img)
time.sleep(0.4)

# 图片填充绿色
img.fill((0, 255, 0))
lcd.display(img)
time.sleep(0.4)

# 图片填充蓝色
img.fill((0, 0, 255))
lcd.display(img)
time.sleep(0.4)

# 图片像素点清除
img.clear()
# 字符显示
img.DispChar("Hello,MaixPy!", 0, 0, color=(255, 255, 255))
img.DispChar("你好,掌控板!", 0, 16, color=(255, 0, 0))

# 画线
img.DispChar("水平线", 0, 40)
img.hline(40, 50, 50, c=(255, 255, 0), thickness=1)
img.DispChar("垂直线", 0, 50)
img.vline(50, 60, 50, c=(0, 255, 0), thickness=2)
img.DispChar("任意线", 100, 50)
img.line(150, 60, 200, 100, c=(0, 255, 255), thickness=1)


#画点
import random
img.DispChar('画点',100,80)
for i in range(20):
    x=random.randint(100,150)
    y=random.randint(80,130)
    img.pixel(x,y,c=(255,255,0))


# 绘制矩形框
img.rect(0, 150, 50, 50, c=(255, 0, 0), thickness=2)
img.DispChar('矩形', 55, 150)
# 绘制实心矩形
img.fill_rect(100, 150, 50, 50, c=(0, 255, 0))
img.DispChar('实心矩形', 155, 150)

# 画中画
img.DispChar('画中画', 120, 220)
img.draw_image(sensor.snapshot(),120,250,x_scale=0.2, y_scale=0.2)


lcd.display(img)
