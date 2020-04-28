.. module:: apu

:mod:`apu` ── 1956应用层驱动库
===========================================

:mod:`apu` 模块提供人工智能项目开发板（1956）电机驱动、机器视觉、LCD屏显示、人工神经网络运算等AI功能函数。



函数
------------

电机驱动
+++++++++++++

提供4路电机驱动。`speed` 范围-100~+100。当为正值时,电机正转,当为负值时,电机反转。

.. data:: m1.speed

.. data:: m2.speed

.. data:: m3.speed

.. data:: m4.speed


.. literalinclude:: /../examples/1956/motor_simple.py
    :caption: 电机驱动示例
    :linenos:

属性
-------------

:mod:`apu` 模块中已提供 :class:`k210.Image` 、 :class:`k210.Sensor` 、 :class:`k210.LCD` 、 :class:`k210.KPU` 类的实例。提供机器视觉、人工智能等k210相关功能函数。
有关更详细的类使用,请查阅相关 :mod:`k210` 模块。

.. attribute:: img = Image()

``Image`` 实例


.. attribute:: lcd = LCD()

``LCD`` 实例

.. literalinclude:: /../examples/1956/img_draw.py
    :caption: image基础绘制
    :linenos:

.. object:: sensor = Sensor()

``Sensor`` 实例

.. literalinclude:: /../examples/1956/snapshot.py
    :caption: 实时摄像
    :linenos:

.. object:: kpu = KPU()

``KPU`` 实例

.. literalinclude:: /../examples/1956/face_detect.py
    :caption: 人脸检测
    :linenos:

