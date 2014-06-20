# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

'''
==========================
API
==========================

赤外線信号を表すJSONについて
=============================

Key: Description

format:
    raw”のみ
freq:
    赤外線信号のサブキャリア周波数を表します。38 または 40 のみ。単位 [kHz]
data:
    赤外線信号は、サブキャリア周波数のオン・オフからなります。IRKitデバイスはオン→オフ間の時間、
    オフ→オン間の時間を 2MHz のカウンタで数えます。dataには、カウンタで数えた数をオン・オフの回数分ならびます。


IRKit Device HTTP API
==========================

- GET /messages

  最も新しい受信した赤外線信号を返します。

  GET /messages が完了すると、保存していた赤外線信号は消去します。
  同じ赤外線信号を2度、続けてGETすることはできません。

- POST /messages

  赤外線信号を送ります。

- POST /keys

  {"clienttoken":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}

  clienttoken を取得します。
  clienttoken を次に IRKit Internet HTTP API の POST /1/keys へのリクエストにのせることで
  clientkey, deviceid を取得することができます。

  詳しくは `IRKit Internet HTTP API <http://getirkit.com/#IRKit-Internet-API>`_ 参照

- POST /wifi

  IRKitは家のWiFiアクセスポイントに接続して動作しますが、
  そのためには、IRKitは家のWiFiアクセスポイントのセキュリティ(WPA2/WEP/NONE)、SSID、パスワードを知る必要があります。

  IRKitにそれを伝える方法は、
  モールス信号を使いマイクを通して伝える方法と、
  IRKit自体がWiFiアクセスポイントになり、それに接続し、IRKitにHTTPリクエストを送る方法
  の2種類があります。

  POST /wifi はその後者に使います。

  家のWiFiアクセスポイントのSSIDなどは、シリアライズしてPOSTリクエストのbodyに入れます。
  シリアライズ方法については、
  keyserializer test にあるJavaScriptの実装と
  \- (NSString *)morseStringRepresentation にあるObjective-Cの実装を見てください。


IRKit Internet HTTP API
=========================

'''

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


class API(object):
    def __init__(self):
        pass
