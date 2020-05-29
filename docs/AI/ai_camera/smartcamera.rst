.. module:: smartcamera

:mod:`smartcamera` ── AI Camera 应用层驱动库
===========================================

:mod:`smartcamera` 模块提供AI Camera模块的摄像头、显示屏、KPU运算、补光灯、按键等应用驱动。

SmartCamera
+++++++++++++++

.. class:: SmartCamera(rx=Pin.P13, tx=Pin.P14)

构建AI Camera应用实例, ``rx`` 、 ``tx`` 参数为定义串口通讯引脚。
 

    .. attribute:: light

    :class:`k210.Light` 的实例,用于控制补光灯亮灭。有关更多类的方法,请查阅该类详情。

    .. attribute:: button

    :class:`k210.Button` 的实例,检测按键状态。有关更多类的方法,请查阅该类详情。

    .. attribute:: image

    :class:`k210.Image` 的实例, `Image` 尺寸为AI Camera的LCD屏的尺寸大小(240*135)。有关更多类的方法,请查阅该类详情。

    .. attribute:: sensor

    :class:`k210.Sensor` 的实例,用于摄像头的操作。有关更多类的方法,请查阅该类详情。

    .. attribute:: lcd

    :class:`k210.LCD` 的实例,用于LCD屏的操作。有关更多类的方法,请查阅该类详情。

    .. attribute:: kpu

    :class:`k210.KPU` 的实例,用于AI模型运行的相关。有关更多类的方法,请查阅该类详情。


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

.. literalinclude:: /../examples/AI_Camera/classifier_flow.py
    :caption: 4类花的图像分类
    :linenos:

上述示例 :download:`4类花图像分类kmodel模型</../examples/Classifier_flower.kmodel>` 下载。
