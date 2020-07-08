
esp_audio 模块
===========================

掌控桌面机器人模块，本模块实现录音、播放功能。支持播放本地或都网络音乐。

:mod:`esp_audio` --- 音频模块

player 类
++++++++++++

播放器类，用于实现播放相关功能。

构建对象
~~~~~~~~~~

.. class:: player(callback, i2c)

    - ``callback``: 播放回调函数，用户须创建一个回调函数，用于处理播放过程中的各种信息。
    - ``i2c``:传一个i2c对象给模块，用于操作解码芯片。

函数
~~~~~~
.. method:: player.info()

获取播放信息

.. method:: player.play(uri)

播放歌曲
    - ``uri``:待播放音频资源。

.. method:: player.stop()

停止播放

.. method:: player.pause()

暂停播放

.. method:: player.resume()

恢复播放

.. method:: player.get_vol()

获取播放器音量

.. method:: player.set_vol(vol)

设置播放器音量
    - ``vol``:音量值。

.. method:: player.get_state()

获取播放状态，播放状态有可能为以下值：
    * ``player.STATUS_UNKNOWN``
    * ``player.STATUS_RUNNING``
    * ``player.STATUS_PAUSED``
    * ``player.STATUS_STOPPED``
    * ``player.STATUS_FINISHED``
    * ``player.CONFUSED``
    * ``player.STATUS_ERROR``

recorder 类
+++++++++++++++

录音类，用于实现录音功能。

构建对象
~~~~~~~~~~

.. class:: recorder(i2c)

    - ``i2c``:传一个i2c对象给模块，用于操作解码芯片。

函数
~~~~~~~~
.. method:: recorder.start(file, format)

启动录音
    - ``file``:录音保存文件。
    - ``format``:保存文件格式。
支持以下录音文件保存格式：`
    * ``recorder.ARM``
    * ``recorder.WAV``

.. method:: recorder.stop()

停止录音

.. method:: recorder.is_running()

返回是否正在录音


示例
-------
