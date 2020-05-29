.. _mpython_classroom_kit_introduce:

.. tang:: 

AI Camera 简介
================

.. image:: /images/ai_camera/ai_camera.png
    :align: center
    :scale: 50%

概述
----

采用高性能AI处理器，具备卷积人工神经网络硬件加速器，可高性能进行卷积人工神经网络运算，实现各种机器视觉能力。
集成200万像素摄像头、彩色显示屏和补光灯，显示屏支持正反两面拼插显示，方便进行不同场景应用。
与掌控板进行串口通讯，配合相关软件及电子模块，完成各类人工智能项目设计与制作，如人脸检测/物体追踪/物体识别/颜色追踪/数字识别等。


技术参数
-------

具有以下特性:

    - UART串口通信
    - 支持MicroPython编程
    - kendryte K210 AI处理器

        - 具备机器视觉能力
        - 具备机器听觉能力和语音识别能力，内置语音处理单元（APU）
        - 具备卷积人工神经网络硬件加速器 KPU ,可高性能进行卷积人工神经网络运算

    - 全彩液晶显示屏:尺寸 240x135 , 支持前显示和后显示两种方式
    - OV2640摄像头:200万像素
    - 补光灯(双LED)
    - 输入按键(一个)
    - 支持 micro SD卡,用于图片、模型等文件储存
    - VCC电源支持3V/5V

接口说明
---------

.. image:: /images/ai_camera/ai_camera_interface.png
    :align: center
    :width: 650

- `LCD屏具有前、后显示两个插口,用户可根据需求选择。`


使用说明
---------

固件升级
++++++++++

.. Important:: AI Camera模块在出厂前已烧录过固件的。非必要情况,如固件出现异常、或固件有重大升级,是无需再次烧录！

1. 准备 kflash_gui K210烧录工具 https://github.com/sipeed/kflash_gui 
2. 下载最新版的 :download:`AI Camera MaixPy固件 </../firmware/owl/owl-2472398.kfpkg>`
3. 参数选择: 选择需要下载的固件；开发板选择 `Sipeed Maix Bit` ; 下载到 `Flash` ; 串口选择该板对应串口号；波特率选择 `4000000` ;
4. 点击下载 

.. figure:: /images/ai_camera/ai_camera_burn.png
    :align: center
    :width: 350

    烧录界面

功能使用
++++++++++

掌控板作为主控,与AI Camera模块通过串口(UART)总线连接。假如,我们使用掌控板的P13,P14作为串口引脚。
在实例 :class:`smartcamera.SmartCamera` 类,通过 `rx` 、`tx` 参数,重定义你的串口引脚。

实例SmartCamera()::

>>> import smartcamera
>>> ai_camera=smartcamera.SmartCamera(rx=Pin.P13,tx=Pin.P14)
>>>





