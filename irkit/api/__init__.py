# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

from six import add_metaclass

from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)

import json
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
        full_path = path.join(self.base_uri, resource_uri)
        logger.debug(full_path + ' params = ' + str(parameters))
        return get(full_path, params=params)

    def post(self, resource_uri, parameters):
        full_path = path.join(self.base_uri, resource_uri)
        # IRKit need raw style params
        raw_params = json.dumps(parameters)
        logger.debug(full_path + ' params = ' + raw_params)

        r = post(full_path, raw_params)
        if r.status_code == 200:
            return json.loads(r.text or '{}')
        raise ValueError(repr(r))


class API(BaseAPI):
    pass
    # messages = Messages('/messages')


class LocalAPI(BaseAPI):
    messages = LocalMessages()
    keys = LocalKeys()
