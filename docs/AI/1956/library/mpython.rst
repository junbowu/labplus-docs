

``mpython`` ── mpython模块(1956)
===========================================


``mpython`` 是模块1956的传感器和输出设备的驱动函数和人工智能应用的相关函数。及兼容掌控板的 `mpython` 模块的相关使用。 
相同的使用方法,在下文将不再说明,可参考掌控板编程手册的 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_ 


.. admonition:: 实验箱与掌控板使用兼容

    - 1956相比掌控板增多一个按键C,共3个物理按键。增加 ``button_c`` 按键对象。


函数
------------


button_[a,b,c]对象
++++++++++++++++++++++

a,b,c按键。button_a/button_b/button_c 是 ``machine.Pin`` 衍生类，继承Pin的方法。更详细的使用方法请查阅 `machine.Pin类 <https://mpython.readthedocs.io/zh/master/library/micropython/machine/machine.Pin.html#machine-pin>`_ 。


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



电机
++++++++++

    .. attribute:: ML1
    .. attribute:: MR2
    .. attribute:: ML2
    .. attribute:: MR2

    :class:`k210.Motor` 的实例,用于控制电机。有关更多类的方法,请查阅该类详情。



apu
++++++++++++++

提供K210机器视觉、摄像头、KPU神经网络处理等相关函数。


    .. attribute:: apu.image

    :class:`k210.Image` 的实例, `Image` 尺寸为LCD屏的尺寸大小。有关更多类的方法,请查阅该类详情。

    .. attribute:: apu.sensor

    :class:`k210.Sensor` 的实例,用于摄像头的操作。有关更多类的方法,请查阅该类详情。

    .. attribute::  apu.lcd

    :class:`k210.LCD` 的实例,用于LCD屏的操作。有关更多类的方法,请查阅该类详情。

    .. attribute::  apu.kpu

    :class:`k210.KPU` 的实例,用于AI模型运行的相关。有关更多类的方法,请查阅该类详情
