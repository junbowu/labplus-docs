
编程手册
====================

掌控板实验箱集成掌控板主控及一体化丰富的传感器和输出设备。集成专门的 `K210` AI处理器,处理视觉图像和神经网络运算,可实现人脸识别、物体追踪等人工智能应用。

在 `Python` 编程上,由于掌控板实验箱项目移植于 `mPython`  ,可较好兼容掌控板的编程。注意, :mod:`mpython` 模块会有所调整变化,但对用户调用几乎无感。其他库使用方法和掌控板一致；
:mod:`mpython_classroom_kit` 模块提供掌控板资源外的实验箱上的传感器驱动和人工智能方法。


类库
------------

.. toctree::
    :maxdepth: 1

    mpython.rst
    display_image.rst
    mpython_classroom_kit.rst


