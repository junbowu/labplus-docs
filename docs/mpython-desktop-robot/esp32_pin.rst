
引脚功能排布
=============
掌控桌面机器人使用esp32-wrover-b模块做为主控，引脚排布如图：

.. image:: /images/mpython-desktop-robot/esp32_pins.png
    :align: center
    :width: 500

- i2c接口
    - 机器人从控mcu,从控mcu控制步进电机、颜色传感器、防跌落传感器、循迹传感器。I2C地址：17。
    - MPU6050 6轴传感器，I2C地址：104
    - MMC5983MA地磁传感器，I2C地址：48
    - codec芯片ES8388，i2c地址：16
    - oled显示屏，I2C地址：60
- RGB LED,控制引脚：P23/IO27
- 顶部按键，控制引脚：P11/IO2
- 电池电量，探测引脚：P3/IO34
- 从机唤醒引脚：P0/IO33
- MPU6050，中断引脚：P8/IO26
- 蜂鸣器，控制引脚：P28/IO34
- 超声波，TRIG引脚：P14/IO19 ECHO引脚：P15/IO21
- 光线：左-控制引脚：P4/IO39 右-控制引脚：P10/IO36