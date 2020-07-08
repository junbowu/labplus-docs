robot模块
============================

robot模块实例
+++++++++++++++++++++++++++

.. automodule:: robot
   :members: color_sensor, tracking_sensor, drop_sensor, sys_config, ultrasonic, robot_motion, hand_color
   :member-order: bysource
      
Tcs34725--颜色传感器类
+++++++++++++++++++++++++++

.. autoclass:: robot.Tcs34725
   :members:
   :undoc-members: True
   :exclude-members:
   :special-members: '__init__' 
   :member-order: bysource

Tracking--循迹类
+++++++++++++++++++++++

.. autoclass:: robot.Tracking
   :members:
   :undoc-members: True
   :exclude-members:
   :special-members: '__init__' 
   :member-order: bysource

DropDetect--防跌落类
++++++++++++++++++++++++++

.. autoclass:: robot.DropDetect
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

RobotMotion--运动类
++++++++++++++++++++++++++++++++

.. autoclass:: robot.RobotMotion
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

RobotHandColor--机器人左右手颜色显示类
+++++++++++++++++++++++++++++++++++++++++++

.. autoclass:: robot.RobotHandColor
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

Ultrasonic--超声波测距传感器类
++++++++++++++++++++++++++++++++++++++++

.. autoclass:: robot.Ultrasonic
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

Button--按键传感器类
++++++++++++++++++++++++++++++++++++++++

.. autoclass:: robot.Button
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

使用示例::

   # 按下按键，打印"hello, world"。
   from robot import Button

   def callback():
      print("hello, world")

   b = Button(callback) #实例Button类，传入用户回调函数。

SysConfig--系统配置类
++++++++++++++++++++++++++++++++

.. autoclass:: robot.SysConfig
   :members:
   :undoc-members: True
   :exclude-members: 
   :special-members: '__init__' 
   :member-order: bysource

