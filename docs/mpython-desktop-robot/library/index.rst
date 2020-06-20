
API接口参考
===========================

.. admonition:: 掌控桌面机器人同掌控板比较

    掌控桌面机器人基于掌控板生态，一些基础功能同掌控板,硬件功能相对掌控板有改动。相应的API有做增删。
        - 修改的硬件功能
            - 去除了按键A，保留B键做为顶部按键。
            - 3轴改为6轴
            - 增加一路光线传感器
            - 麦克风做为codec芯片的录音输入。
            - RGB LED增加到8个，做为机器人的左右手装饰。

        - 新增的功能
            - 机器人行走功能
            - 颜色传感器
            - 防跌落检测
            - 机器人循迹检测功能
            - 超声波测距功能
            - 低功耗控制

本API接口参考文档针对新增的硬件功能特性。掌控板API接口文档，请参阅 `mpython模块 <https://mpython.readthedocs.io/zh/master/library/mPython/mpython.html>`_ 


.. toctree::
    :maxdepth: 1

    robot
    dueros
    esp_audio

    


    
