# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )


from argparse import ArgumentParser


from irkit.resolve import resolve_irkit_addresses
from irkit._info import VERSION



CMD_PARSER = ArgumentParser(description='IRKit CLI Client for Python. v{0}'.format(VERSION))


subparsers = CMD_PARSER.add_subparsers(help='sub-command help')


def local_func(args):
    # from irkit import LocalAPI
    # base_uri = resolve_irkit_addresses()[0]
    # api = LocalAPI(base_uri)
    if args.keys:
        # print(api.keys.post())
        print('this is your key')
        return
    if args.send:
        print('send ' + args.send)


LOCAL_PARSER = subparsers.add_parser('local', help='api for locals.')
LOCAL_PARSER.add_argument('--keys', action='store_true', help='get a client token.')
LOCAL_PARSER.add_argument('--send', help='send signals.')
LOCAL_PARSER.set_defaults(func=local_func)


INTERNET = subparsers.add_parser('global', help='api for internets.')


args = CMD_PARSER.parse_args()
args.func(args)
