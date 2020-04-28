.. module:: smartcamera

:mod:`smartcamera` ── AI Camera 应用层驱动库
===========================================

:mod:`smartcamera` 模块提供AI Camera模块的摄像头、显示屏、KPU运算、补光灯、按键等应用驱动。

类
------------

补光灯
+++++++++

.. class:: Light()


    .. method:: Light.on()

    摄像头补光灯控制,打开。


    .. method:: Light.off()

    摄像头补光灯控制,关闭。


按键
+++++++++

.. class:: Button()

    .. method:: Button.is_pressed()

    返回当前是否按住。 ``True`` 表示按键按下，``False`` 则未按下。

    .. method:: Button.was_pressed()

    返回 ``True`` 或 ``False`` 指示自设备启动以来或上次调用此方法以来是否按下按钮。调用此方法将清除按下状态，因此必须再次按下按钮，然后才能再次返回 ``True`` 。

    .. method:: Button.get_presses()

    返回按键的运行总数，并在返回之前将该总数重置为零。

SmartCamera
+++++++++++++++

.. class:: SmartCamera(rx=Pin.P13, tx=Pin.P14)

构建AI Camera应用实例, ``rx`` 、 ``tx`` 参数为定义串口通讯引脚。
 
``SmartCamera`` 类里会提供 :class:`Light` 、:class:`Button` 、:class:`k210.Image` 、 :class:`k210.Sensor` 、 :class:`k210.LCD` 、 :class:`k210.KPU` 类的实例。用于机器视觉、人工智能等k210相关功能函数。


    .. attribute:: light

    :class:`Light` 实例,有关更多类的方法,请查阅该类说明。

    .. attribute:: button

    :class:`Button` 实例,有关更多类的方法,请查阅该类说明。

    .. attribute:: img

    实例 尺寸为240*130的 :class:`k210.Image` 实例 ,有关更多类的方法,请查阅该类说明。

    .. attribute:: sensor

    :class:`k210.Sensor` 实例,有关更多类的方法,请查阅该类说明。

    .. attribute:: lcd

    :class:`k210.LCD` 实例,有关更多类的方法,请查阅该类说明。

    .. attribute:: kpu

    :class:`k210.KPU` 实例,有关更多类的方法,请查阅该类说明。


.. literalinclude:: /../examples/AI_Camera/snapshot.py
    :caption: 实时摄像
    :linenos:

.. literalinclude:: /../examples/AI_Camera/image_draw.py
    :caption: image绘图操作
    :linenos:


.. literalinclude:: /../examples/AI_Camera/face_detect.py
    :caption: 人脸检测
    :linenos:



.. literalinclude:: /../examples/AI_Camera/20classes.py
    :caption: 20类检测
    :linenos: