# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )


class Client(object):
    def __init__(self, ):
        pass


if __name__ == '__main__':
    api = API()
    print(api.message)
    print(api.get('http://docs.python-requests.org/en/latest/user/quickstart/').text.encode('utf-8'))
