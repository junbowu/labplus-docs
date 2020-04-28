.. module:: apu

:mod:`apu` ─── 板载和AI相关功能函数
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


机器视觉
+++++++++++++

图像处理相关

.. method:: img.DispChar(text, x, y, color=(255, 255, 255))

在图像中的(x, y)位置开始绘制文本。字体采用 `Google Noto Sans CJK <http://www.google.cn/get/noto/help/cjk/>`_ 开源无衬线字体字体。字体高度16像素点,支持英文,简体中文繁体中文，日文和韩文语言。

    - ``text`` -- 绘制的文本
    -  ``x`` 、 ``y`` -- 起点坐标
    - ``color`` -- 字体颜色

.. method:: img.pixel( x, y, c)

设置图像像素点颜色

    -  ``x`` 、 ``y`` -- 像素点坐标
    - ``c`` -- 颜色


.. method:: img.hline(x, y, w, c=(255, 255, 255), thickness=1)

在图像中绘制水平线

    -  ``x`` 、 ``y`` -- 起点坐标
    - ``w`` -- 线宽
    - ``thickness`` -- 线粗

.. method:: img.vline(x, y, h, c=(255, 255, 255), thickness=1)

在图像中绘制垂直线

    -  ``x`` 、 ``y`` -- 起点坐标
    - ``w`` -- 线高
    - ``thickness`` -- 线粗


.. method:: img.line(x0, y0, x1, y1, c=(255, 255, 255), thickness=1)

在图像中绘制任意线

    - ``x0`` 、 ``y0`` -- 起点位置
    - ``x1`` 、 ``y1`` -- 终点位置
    - ``c`` -- 颜色
    - ``thickness`` -- 线粗

.. method:: img.rect(x, y, w, h,c=(255, 255, 255), thickness=1)

在图像中绘制矩形框

    - ``x`` 、``y`` -- 左上坐标 
    - ``w`` 、 ``h`` -- 宽,高
    - ``c`` -- 颜色
    - ``thickness`` -- 线粗

.. method:: img.fill_rect(x, y, w, h,c=(255, 255, 255))

在图像中绘制实心矩形

    - ``x`` 、``y`` -- 左上坐标 
    - ``w`` 、 ``h`` -- 宽,高
    - ``c`` -- 颜色
    - ``thickness`` -- 线粗

.. method:: img.draw_image(image, x, y, x_scale=1.0, y_scale=1.0, alpha=256)

画中画,在图像中绘制一个 `image` 。

    - ``x`` 、``y`` -- 左上坐标 
    - ``x_scale`` --  控制绘制的图像在x方向的缩放(浮点数)
    - ``y_scale`` --  控制绘制的图像在y方向的缩放(浮点数)
    - ``alpha`` --  控制另一幅图像与这幅图像的混合程度。 alpha 应该是0到256之间的一个整数值。接近零的值会将更多其他图像混合到该图像中，而接近256的值则相反。

.. method:: img.clear()

将图像中的所有像素设置为零


.. literalinclude:: /../examples/1956/img_draw.py
    :caption: image基础绘制
    :linenos:


摄像头
+++++++++++++

传感器模块，进行摄像头配置及图像抓取等，用于控制开发板摄像头完成摄像任务。

.. method:: sensor.snapshot()

拍摄图像,返回Image对象。

.. method:: sensor.set_vflip(enable)

打开（True）或关闭（False）垂直翻转模式。默认关闭。

.. method:: sensor.set_hmirror(enable)

打开（True）或关闭（False）水平镜像模式。默认关闭。


.. literalinclude:: /../examples/1956/snapshot.py
    :caption: 实时摄像
    :linenos:


LCD
+++++++++++++

.. method:: lcd.display(image, roi=None, offset=None)

在液晶屏上显示图片。

    - ``image`` -- 为Image对象
    - ``roi``  -- 一个感兴趣区域的矩形元组(x, y, w, h)。若未指定，即为图像矩形

.. method:: lcd.clear(c=(0, 0, 0))

将液晶屏清空为黑色或者指定的颜色

KPU
+++++++++++++


KPU是通用的神经网络处理器，它可以在低功耗的情况下实现卷积神经网络计算，时时获取被检测目标的大小、坐标和种类，对人脸或者物体进行检测和分类。

KPU 具备以下几个特点：

    - 支持主流训练框架按照特定限制规则训练出来的定点化模型
    - 对网络层数无直接限制，支持每层卷积神经网络参数单独配置，包括输入输出通道数目、输入输 出行宽列高
    - 支持两种卷积内核 1x1 和 3x3
    - 支持任意形式的激活函数
    - 实时工作时最大支持神经网络参数大小为 5.5MiB 到 5.9MiB
    - 非实时工作时最大支持网络参数大小为（Flash 容量-软件体积）


.. method:: kpu.load(path)

从flash或者文件系统中加载模型,。`path` 可以是模型在 flash 中的偏移大小,如 0xd00000 表示模型烧录在13M起始的地方,或者模型在文件系统中为文件名， 如 "/sd/xxx.kmodel"

.. method:: kpu.init_yolo2(threshold, nms_value, anchor_num, anchor)

为yolo2网络模型传入初始化参数。

    - ``threshold`` -- 概率阈值
    - ``nms_value`` -- box_iou 门限
    - ``anchor_num`` -- 锚点数
    - ``anchor`` -- 锚点参数与模型参数一致

.. method:: kpu.run_yolo2(image)

运行yolo2网络。`image` 为Image对象,从 sensor 采集到的图像。

.. method:: kpu.forward(image)

计算已加载的网络模型，输出目标层的特征图。`image` 为Image对象,从 sensor 采集到的图像。


.. method:: kpu.deinit()

反初始化

.. literalinclude:: /../examples/1956/face_detect.py
    :caption: 人脸检测
    :linenos:

