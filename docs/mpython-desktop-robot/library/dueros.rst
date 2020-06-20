
dueros 模块
===========================

掌控桌面机器人高阶应用，加载本模块后，可让机器人具备智能音箱功能，提高本产品的可玩性。

使用本模块时，用户须自行在百度注册一个帐号，获取profile文件，这样才能获取百度提供的语音服务功能。:ref:`百度profile获取<get_profile>`.

:mod:`dueros` --- 百度云语音服务

函数
----

.. method:: dueros.dueros_init(i2c)

dueros模块初始化
    - ``i2c``:传一个i2c对象给模块，用于操作解码芯片。

.. method:: dueros.get_vol()

获取播放器音量

.. method:: dueros.set_vol(vol)

设置播放器音量
    - ``vol``:音量值，取值范围0-100。

示例
----
::

    import dueros
    dueros.dueros_init(i2c)
    dueros.set_vol(70)
    print(dueros.get_vol())
