# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

'''
'''

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

import json

from .base import Resources, InfraredLightEntity


class Messages(Resources):
    '''
    - GET /messages

      最も新しい受信した赤外線信号を返します。

      GET /messages が完了すると、保存していた赤外線信号は消去します。
      同じ赤外線信号を2度、続けてGETすることはできません。

      return InfraredLightEntity

    - POST /messages

      赤外線信号を送ります。
    '''
    uri = 'messages'

    def get(self):
        # () -> InfraredLightEntity
        r = self.client.get(Messages.uri, {})
        if r.status_code == 200:
            result = r.text.decode('utf-8')
            logger.debug('retrieve result is:' + result)
            return InfraredLightEntity(
                responsed_json=json.loads(result or '{}')
            )
        else:
            raise ValueError(repr(r))

    def post(self, parameters):
        assert isinstance(parameters, InfraredLightEntity)
        return self.client.post(Messages.uri, parameters.as_dict())


class Keys(Resources):
    '''
    - POST /keys

      clienttoken を取得します。
      clienttoken を次に IRKit Internet HTTP API の POST /1/keys へのリクエストにのせることで
      clientkey, deviceid を取得することができます。

      詳しくは `IRKit Internet HTTP API <http://getirkit.com/#IRKit-Internet-API>`_ 参照

      return {"clienttoken":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"}
    '''
    uri = 'keys'

    def post(self):
        return self.client.post(Keys.uri, {})


class Wifi(Resources):
    '''
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
    '''

    def post(self, parameters):
        NotImplementedError("not implemented yet")
