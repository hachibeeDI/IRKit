#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

import json
from argparse import ArgumentParser


from irkit.resolve import resolve_irkit_addresses
from irkit._info import VERSION


def save_signal(name, signal):
    from os import environ, path, makedirs

    config_root = path.join(environ['HOME'], '.config')
    if not path.exists(config_root):
        makedirs(config_root)
    dir_to_save = path.join(config_root, 'irkit-py')
    if not path.exists(dir_to_save):
        makedirs(dir_to_save)

    store_file = path.join(dir_to_save, 'signal.json')
    # initialize if no store
    if not path.exists(dir_to_save):
        with open(store_file, 'w') as f:
            f.write('{}')

    with open(store_file, 'r+') as f:
        config = json.loads(f.read())
        config[name] = signal

        f.seek(0)
        f.write(json.dumps(config))


def get_signals():
    # type: (str) -> dict
    """
    :exception: IOError
    """
    from os import environ, path

    with open(path.join(environ['HOME'], '.config', 'irkit-py', 'signal.json'), 'r') as f:
        return json.loads(f.read())


def saved_signals():
    return get_signals().keys()


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


INTERNET = subparsers.add_parser('global', help='api for internets.')


args = CMD_PARSER.parse_args()
args.func(args)
