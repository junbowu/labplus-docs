.. module:: mpython

:mod:`mpython` ── mpython模块(1956)
===========================================


``mpython`` 提供掌控板板载资源和相关的功能函数。与掌控板的 `mpython` 模块,会些细微的区别。
相同的使用方法,在下文将不再说明,可参考掌控板编程手册的 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_ 

.. Attention:: 
    - 1956相比掌控板增多一个按键C,共3个物理按键
    - 加速度传感器升级为MPU6050空间运动传感器

函数
------------


button_[a,b,c]对象
++++++++++++++++++++++

a,b,c按键。button_a/button_b/button_c 是 ``machine.Pin`` 衍生类，继承Pin的方法。更详细的使用方法请查阅 `machine.Pin类 <https://mpython.readthedocs.io/zh/master/library/micropython/machine/machine.Pin.html#machine-pin>`_ 。


运动传感器
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