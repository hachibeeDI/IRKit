# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

from six import add_metaclass

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


from abc import ABCMeta


@add_metaclass(ABCMeta)
class Resources(object):
    ''' API Resources '''
    uri = None

    def __init__(self):
        self.client = None

    def __get__(self, instance, owner):
        self.client = instance
        return self

    def __set__(self, instance, value):
        raise NotImplementedError

    def get(self, parameters):
        raise NotImplementedError

    def post(self, parameters):
        raise NotImplementedError


class InfraredLightEntity(object):
    '''
    赤外線信号を表すJSONについて
    =============================

    format:
        raw”のみ
    freq:
        赤外線信号のサブキャリア周波数を表します。
        38 または 40 のみ。単位 [kHz]
    data:
        赤外線信号は、サブキャリア周波数のオン・オフからなります。
        IRKitデバイスはオン→オフ間の時間、オフ→オン間の時間を 2MHz のカウンタで数えます。
        dataには、カウンタで数えた数をオン・オフの回数分ならびます。
    '''
    def __init__(self, responsed_json=None, format=None, freq=None, data=None, ):
        if responsed_json:
            self.format = responsed_json['format']
            self.freq = responsed_json['freq']
            self.data = responsed_json['data']
        else:
            self.format = format
            self.freq = freq
            self.data = data

    def as_dict(self):
        return self.__dict__
