from apu import *
import time

# m1正转,速度100
m1.speed = 100
time.sleep(2)
# m1反转,速度100
m1.speed = -100
time.sleep(2)
# m1电机停止
m1.speed = 0
