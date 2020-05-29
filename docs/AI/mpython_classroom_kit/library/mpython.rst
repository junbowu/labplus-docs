

``mpython`` --- mpython模块(掌控板实验箱)
===========================================


``mpython`` 是掌控板板实验箱兼容掌控板主控的模块,提供掌控板板载资源和相关的功能函数。与掌控板的 `mpython` 模块,会些细微的区别。
相同的使用方法,在下文将不再说明,可参考掌控板的 :ref:`mpython模块说明 <mpython.py>` 。

.. Attention:: 

    掌控板内置的光线传感器、麦克风、蜂鸣器,在实验箱上位置有所变化。除麦克风, `sound.read()` 前须要 `sound.init()` 。其他使用方式和掌控板是一样的。


函数
------------

运动
+++++++++++


可以获取MPU6050空间运动传感器当前的3轴加速度、角速度和欧拉角、四元数。通过这些数据,你可以很容易的获取物体的运动姿态。

.. method:: motion.get_accel()

返回当前三轴加速度元组(x,y,z)。单位g,范围-2~+2g。

.. method:: motion.get_gyro()

返回当前三轴角速度元组(x,y,z),范围±500°/秒

.. method:: motion.get_euler()

返回当前欧拉角元组(Pitch,Roll,Yaw),单位角度

.. method:: motion.get_quat()

返回当前四元数元组(w,x,y,z)


掌控板触摸按键
++++++++++++++

用法和掌控板一样,用 ``read()`` 获取模拟值。由于实验箱不支持返回模拟值,只能返回0或1023,这点须注意！

.. method:: touchPad_[P,Y,T,H,O,N].read()

返回触摸值(0或1023)

RGB LED
++++++++++++++

掌控板实验箱集成5x5 RGB LED矩阵,有25颗灯珠,而掌控板上只有3颗。在使用上和掌控板是一样的。
有关跟多的 ``rgb`` 函数,参考掌控板的 :ref:`mpython模块说明 <mpython.py>` 。


麦克风
++++++++++++++

.. admonition:: 区别

    由于实验箱增加音频编解码芯片专门处理音频数据。所以在 ``sound.read()`` 读取声音响度前,须要初始化设置。

.. staticmethod:: sound.init()

初始化,开启音频解码

.. staticmethod:: sound.read()

获取声音响度

.. staticmethod:: sound.deinit()

关闭音频解码


