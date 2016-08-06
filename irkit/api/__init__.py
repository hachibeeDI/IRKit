# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

from six import add_metaclass

from logging import getLogger
logger = getLogger(__name__)

import json
from os import path
from abc import ABCMeta

from .local import (
    Messages as LocalMessages,
    Keys as LocalKeys,
)
from .internet import (
    Messages as InternetMessages,
)

from requests import (
    get,
    post,
)



@add_metaclass(ABCMeta)
class BaseAPI(object):

    def __init__(self, host, is_https=False):
        if is_https:
            self.base_uri = 'https://' + host
        else:
            self.base_uri = 'http://' + host

    def get(self, resource_uri, parameters=None):
        logger.debug('url is ' + self.base_uri)

        params = parameters or {}
        full_path = path.join(self.base_uri, resource_uri)

        r = get(full_path, params=params)
        logger.debug('request to {}: {}'.format(r.request.url, r.text))
        if r.status_code == 200:
            result = r.text.decode('utf-8')
            return json.loads(result or '{}')
        else:
            raise ValueError(r.text)


    def post(self, resource_uri, raw_payload=None, payload=None):
        """
        IRKit basically accept JSON-Encoded data so you should use :raw_payload:.
        But InternetAPI use form parameter with encoded data so you should use :payload:.
        """
        logger.debug('url is ' + self.base_uri)

        full_path = path.join(self.base_uri, resource_uri)

        if raw_payload:
            param = json.dumps(raw_payload)
        else:
            param = payload

        logger.debug(full_path + ' params = ' + str(param))

        r = post(full_path, param)
        if r.status_code == 200:
            return json.loads(r.text or '{}')
        else:
            logger.error(r.text)
            raise ValueError(r.text)


class API(BaseAPI):
    pass
    # messages = Messages('/messages')


class LocalAPI(BaseAPI):
    messages = LocalMessages()
    keys = LocalKeys()


class InternetAPI(BaseAPI):
    messages = InternetMessages()

    def __init__(self):
        super(InternetAPI,  self).__init__('api.getirkit.com', True)
