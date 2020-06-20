.. _get_profile:

获取dueros profile
==================

本模块基于百度dueros人工智能实现。使用前，必须完成wifi和duer_profile配置，duer_profile文件须通过注册百度户并创建应用获取，以下为获取profile过程。

#. 注册百度帐户

    `百度帐户注册 <https://passport.baidu.com/v2/?login&u=https%3A%2F%2Fdueros.baidu.com%2Fdidp%2Fmain%2Findex>`_ 

    .. image:: /images/mpython-desktop-robot/baidu_logo.png
        :align: center
        :width: 200


#. 进入dueros设备控制台配置设备
    `登陆页面 <https://dueros.baidu.com/didp/main/index>`_ 

    .. image:: /images/mpython-desktop-robot/baidu_logon_in.png
        :align: center
        :width: 200

    用注册的帐号登陆。登陆后找到“轻量级设备”进入。

    .. image:: /images/mpython-desktop-robot/light_device.png
        :align: center
        :width: 200

    .. image:: /images/mpython-desktop-robot/to_light_dev.png
        :align: center
        :width: 200

    `设备控制台页面 <https://dueros.baidu.com/didp/product/listview>`_ 

#. 配置一个新设备
    .. image:: /images/mpython-desktop-robot/device_control.png
        :align: center
        :width: 200  
    点击“配置新设备”，添加一个新设备。

    .. image:: /images/mpython-desktop-robot/new_device.png
        :align: center
        :width: 200  
    选择“故事机”, 下一步

    .. image:: /images/mpython-desktop-robot/os_select.png
        :align: center
        :width: 200     
    系统选“FreeRtOS",下一步

    .. image:: /images/mpython-desktop-robot/product_name.png
        :align: center
        :width: 200   
    输入自定义的产品名，例如”掌控小生“，申请ClientID。

#. 获取duer_profile
    接下来的页面中，点击“设备端开发“。

    .. image:: /images/mpython-desktop-robot/baidu_profile.png
        :align: center
        :width: 200  
    点击profile下载duer_profile文件, 获取的profile压缩包解压，里面有20个profile文件，我们可用其中任意一个。
