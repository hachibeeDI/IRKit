# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

import json
from argparse import ArgumentParser


from irkit.resolve import resolve_irkit_addresses
from irkit._info import VERSION



desc = """
IRKit CLI Client for Python. v{0} See also http://getirkit.com/#IRKit-Device-API
""".format(VERSION)
CMD_PARSER = ArgumentParser(description=desc)


subparsers = CMD_PARSER.add_subparsers(help='sub-command help')


def local_func(args):
    from irkit.api import LocalAPI
    base_uri = resolve_irkit_addresses()[0]
    if args.host:
        print(base_uri)
        return


    api = LocalAPI(base_uri)
    if args.keys:
        print(api.keys.post())
        print('this is your key')
        return
    elif args.send:
        raw_data = json.loads(args.send)
        result = api.messages.post(raw_data)
        print('')
        print('send signal: ' + unicode(result))
        return
    elif args.retrieve:
        result = api.messages.get()
        print('')
        print('retrieve: ' + str(result))
        return
    else:
        print('need argument. see help')
        return


LOCAL_PARSER = subparsers.add_parser('local', help='api for locals.')
LOCAL_PARSER.add_argument('--host', action='store_true', help='show irkit host')
LOCAL_PARSER.add_argument('--keys', action='store_true', help='get a client token.')
LOCAL_PARSER.add_argument('--retrieve', action='store_true', help='retrieve a singnal')
LOCAL_PARSER.add_argument('--send', help='send a signal data or api response')
LOCAL_PARSER.set_defaults(func=local_func)


INTERNET = subparsers.add_parser('global', help='api for internets.')


args = CMD_PARSER.parse_args()
args.func(args)
