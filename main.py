#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

import json
from argparse import ArgumentParser


from irkit.resolve import resolve_irkit_addresses
from irkit._info import VERSION

from irkit._command_utils.storage import (
    get_signals,
    save_signal,
)


desc = """
IRKit CLI Client for Python. v{0} See also http://getirkit.com/#IRKit-Device-API
""".format(VERSION)
CMD_PARSER = ArgumentParser(description=desc)


subparsers = CMD_PARSER.add_subparsers(help='sub-command help')


def local_func(args):
    from irkit.api import LocalAPI

    if args.verbose:
        from logging import DEBUG
        from irkit import logger, handler
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)

    if args.list:
        for s in get_signals():
            print(s)
        return

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
        # FIXME: I hate this style
        value_to_send = None
        try:
            # TODO: check parsable before load
            value_to_send = json.loads(args.send)
        except ValueError:
            # if argument is just string this command assume that is key name of data store
            try:
                value_to_send = get_signals()[args.send]
            except (IOError, KeyError):
                return print('invalid name "{}" is passed. string should be key of signal.json'.format(args.send))

        result = api.messages.post(value_to_send)
        print('')
        return print('signal was sent')

    elif args.retrieve:
        result = api.messages.get()
        if result.is_empty():
            return print('retrieve empty data. you should send signal to irkit before retrieve.')

        if args.save:
            save_signal(args.save, result.as_dict())
            print('save signal as {} in ~/.config/irkit-py/signal.json'.format(args.save))
        print(str(result))
        return

    else:
        print('need argument. see help')
        return


"""
sub command for local API
"""
LOCAL_PARSER = subparsers.add_parser('local', help='api for locals.')
LOCAL_PARSER.add_argument('--host', action='store_true', help='show irkit host')
LOCAL_PARSER.add_argument('-k', '--keys', action='store_true', help='get a client token.')
LOCAL_PARSER.add_argument('-r', '--retrieve', action='store_true', help='retrieve a signal')
LOCAL_PARSER.add_argument(
    '--save',
    action='store',
    default='',
    metavar='signal-name',
    help='you should appoint a name. save retrieved signal to ~/.config/irkit-py/signal.json with name',
)
LOCAL_PARSER.add_argument('-l', '--list', action='store_true',  help='list of stored signals')
LOCAL_PARSER.add_argument('-s', '--send', metavar='signal-info', help='send a signal. that excepted as json response or raw_data or key name of store')
# TODO: verbose level hint: add_argument(action='count')
LOCAL_PARSER.add_argument('-v', '--verbose', action='store_true', help='put verbose logs')
LOCAL_PARSER.set_defaults(func=local_func)


def internet_func(args):
    from irkit.api import InternetAPI

    if args.verbose:
        from logging import DEBUG
        from irkit import logger, handler
        handler.setLevel(DEBUG)
        logger.setLevel(DEBUG)

    api = InternetAPI()
    # if args.keys:
    #     print(api.keys.post())
    #     print('this is your key')
    #     return

    if args.send:
        key = args.client_key
        if key is None:
            return print('retrieve over the internet needs client-key')
        print('key is ', key)
        device_id = args.device_id
        if key is None:
            return print('retrieve over the internet needs device-id')
        print('device id is ', device_id)

        # FIXME: I hate this style
        value_to_send = None
        try:
            # TODO: check parsable before load
            value_to_send = json.loads(args.send)
        except ValueError:
            # if argument is just string this command assume that is key name of data store
            try:
                value_to_send = get_signals()[args.send]
            except (IOError, KeyError):
                return print('invalid name "{}" is passed. string should be key of signal.json'.format(args.send))

        result = api.messages.post(value_to_send, key, device_id)
        print('')
        return print('signal was sent')

    elif args.retrieve:
        key = args.client_key
        if key is None:
            return print('retrieve over the internet needs client-key')

        result = api.messages.get(key)
        if result.is_empty():
            return print('retrieve empty data. you should send signal to irkit before retrieve.')

        if args.save:
            save_signal(args.save, result.as_dict())
            print('save signal as {} in ~/.config/irkit-py/signal.json'.format(args.save))
        print(str(result))
        return

    else:
        print('need argument. see help')
        return


"""
sub command for internet API
"""
INTERNET = subparsers.add_parser('internet', help='api for internets.')
INTERNET.add_argument('-r', '--retrieve', action='store_true', help='retrieve a signal')
INTERNET.add_argument(
    '-s',
    '--send',
    metavar='signal-info',
    help='send a signal. that excepted as json response or raw_data or key name of store',
)
# I'm not sure who would like to retrieve and save IR data via internet...
INTERNET.add_argument(
    '--save',
    action='store',
    default='',
    metavar='signal-name',
    help='you should appoint a name. save retrieved signal to ~/.config/irkit-py/signal.json with name',
)
INTERNET.add_argument('-c', '--client-key', help='client key')
INTERNET.add_argument('-d', '--device-id', help='device id')
INTERNET.add_argument('-v', '--verbose', action='store_true', help='put verbose logs')
INTERNET.set_defaults(func=internet_func)


args = CMD_PARSER.parse_args()
args.func(args)
