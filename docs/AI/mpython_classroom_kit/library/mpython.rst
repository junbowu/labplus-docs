

``mpython`` ── mpython模块(实验箱)
===========================================

``mpython`` 是模块提供实验箱上的传感器和输出设备的驱动函数和人工智能应用的相关函数。及兼容掌控板的 `mpython` 模块的相关使用。 
与掌控板上的 `mpython` 模块相同的使用方法,在下文将不再说明,可参考掌控板的 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_。

.. admonition:: 实验箱与掌控板使用兼容

    - 掌控板内置的光线传感器、麦克风、蜂鸣器,在实验箱上位置有所变化。
    - 由于由于实验箱增加音频编解码芯片专门处理音频数据,区别于掌控板的模拟的音频输入。使用 `sound` 前需要对音频解码芯片进行初始化配置。顾增加 , :mod:`sound.init()` 初始化函数。
    - 实验箱的蜂鸣器控制引脚为P28(区别于掌控板控制引脚P6)。
    - 触摸按键的硬件电路上的不同,实验箱采用外设电容触摸按键扫描芯片。``touchPad_[P,Y,T,H,O,N].read()`` 只能返回未按下和按下两种状态(0、1023)
    - 掌控板实验箱集成5x5 RGB LED矩阵,有25颗灯珠,替换掌控板上3颗RGB。控制引脚都是P7。你可以使用 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_ 的 `rgb` 操作,或者使用 :mod:`rgbLED5x5` 模块。
函数
------------

gyroscope(角速度)
+++++++++++++++

通过MPU6050传感器获取器角速度

    .. method:: gyroscope.get_x()

    返回x轴的角速度,范围±500,单位°/秒

    .. method:: gyroscope.get_y()

    返回y轴的角速度,范围±500,单位°/秒

    .. method:: gyroscope.get_z()

    返回z轴的角速度,范围±500,单位°/秒


motion(运动)
+++++++++++++++

通过MPU6050空间运动传感器的原始数据,计算得出欧拉角、四元数。以便你可以很容易的获取物体的运动姿态。


    .. method:: motion.get_euler()

    返回当前欧拉角元组(Pitch,Roll,Yaw),单位角度

    .. method:: motion.get_quat()

    返回当前四元数元组(w,x,y,zs)


掌控板触摸按键
++++++++++++++

触摸按键电路上,实验箱和掌控板有所不同。实验箱采用外设电容触摸按键扫描芯片,没有使用到掌控板的触摸引脚。触摸按键值的读取函数接口和掌控板是一样的,但,芯片不支持返回模拟值,故只能返回
0或1023(未按下,按下两种状态),这点须注意的。


    .. method:: touchPad_[P,Y,T,H,O,N].read()

返回触摸值(0或1023)

RGB LED
++++++++++++++

掌控板实验箱集成5x5 RGB LED矩阵,有25颗灯珠,替换掌控板上3颗RGB,控制引脚都为P7。在使用上和掌控板是一样的。
有关更多的 ``rgb`` 函数,参考掌控板的 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_。
或者使用 :mod:`rgbLED5x5` 模块。

麦克风
++++++++++++++

    .. admonition:: 区别

        由于实验箱增加音频编解码芯片专门处理音频数据。所以在 ``sound.read()`` 读取声音响度前,须要初始化设置。

    .. method:: sound.init()

    初始化,开启音频解码

    .. method:: sound.read()

    获取声音响度

    .. method:: sound.deinit()

    关闭音频解码


实验箱的外设设备
++++++++++++++

    .. method:: pir.value()

    返回人体红外触发值。当为1时,表示已触发。

    .. method:: slider_res.read()

    返回滑杆电阻采样值。范围0~4095。

    .. attribute:: bme280


    BME280是一款集成温度、湿度、气压，三位一体的环境传感器。具有高精度，多功能，小尺寸等特点。该传感器非常适合各种天气/环境传感。
    精度为±3％，气压为±1 hPa绝对精度，温度精度为±1.0°C。由于压力随高度变化，压力测量结果非常好，您也可以将其用作±1米或更高精度的高度计！

    使用方法,可参考掌控板的 `mpython模块的bme280 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html#bme280>`_。

apu
++++++++++++++

提供实验箱上K210控制的外设驱动函数和人工智能应用的相关函数。


    .. attribute:: motor

    :class:`k210.Motor` 的实例,用于控制电机。有关更多类的方法,请查阅该类详情。

    .. attribute:: ultrasonic

    :class:`k210.Ultrasonic` 的实例,获取超声波的距离值。有关更多类的方法,请查阅该类详情。

    .. attribute:: light

    :class:`k210.Light` 的实例,用于控制补光灯亮灭。有关更多类的方法,请查阅该类详情。

    .. attribute:: btn_left
    .. attribute:: btn_right
    .. attribute:: btn_up
    .. attribute:: btn_down
    .. attribute:: btn_ok

    :class:`k210.Button` 的实例,检测按键状态。有关更多类的方法,请查阅该类详情。


    .. attribute:: image

    :class:`k210.Image` 的实例, `Image` 尺寸为LCD屏的尺寸大小。有关更多类的方法,请查阅该类详情。

    .. attribute:: sensor

    :class:`k210.Sensor` 的实例,用于摄像头的操作。有关更多类的方法,请查阅该类详情。

    .. attribute:: lcd

    :class:`k210.LCD` 的实例,用于LCD屏的操作。有关更多类的方法,请查阅该类详情。

    .. attribute:: kpu

    :class:`k210.KPU` 的实例,用于AI模型运行的相关。有关更多类的方法,请查阅该类详情