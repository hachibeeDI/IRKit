# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

from six import add_metaclass

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)


from os import path
from abc import ABCMeta


from .local import (
    Messages as LocalMessages,
    Keys as LocalKeys,
)

from requests import (
    get,
    post,
)



@add_metaclass(ABCMeta)
class BaseAPI(object):

    def __init__(self, host):
        self.base_uri = 'http://' + host

    def get(self, resource_uri, parameters=None):
        params = parameters or {}
        return get(self.base_uri + resource_uri, params=params)

    def post(self, resource_uri, parameters):
        return post(path.join(self.base_uri, resource_uri), params=parameters)


class API(BaseAPI):
    pass
    # messages = Messages('/messages')


class LocalAPI(BaseAPI):
    messages = LocalMessages()
    keys = LocalKeys()
