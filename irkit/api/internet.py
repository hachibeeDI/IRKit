# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )


from logging import getLogger
logger = getLogger(__name__)

import json

from .base import Resources, InfraredLightEntity


class Messages(Resources):
    uri = '1/messages'

    def get(self, client_key):
        # () -> InfraredLightEntity
        r = self.client.get(Messages.uri, {'clientkey': client_key, 'clear': 1})
        # InternetAPI returns difference structure from local API
        return InfraredLightEntity(responsed_json=r['message'])

    def post(self, message, client_key, device_id):
        """
        see http://getirkit.com/#IRKit-Internet-POST-1-messages
        """
        if isinstance(message, list):
            message = {
                'format': 'raw',
                'freq': 38,
                'data': message,
            }
        elif isinstance(message, InfraredLightEntity):
            message = message.as_dict()

        parameters = {
            'clientkey': client_key,
            'deviceid': device_id,
            'message': json.dumps(message),
        }
        return self.client.post(Messages.uri, payload=parameters)


class Keys(Resources):
    uri = '1/keys'

    def post(self, client_token):
        return self.client.post(Keys.uri, {'clienttoken': client_token})
