# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

import json
from os import environ, path, makedirs


def save_signal(name, signal):

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

    with open(path.join(environ['HOME'], '.config', 'irkit-py', 'signal.json'), 'r') as f:
        return json.loads(f.read())
