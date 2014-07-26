# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )


from argparse import ArgumentParser


from .irkit.resolve import resolve_irkit_addresses
from .irkit.info import VERSION

CMD_PARSER = ArgumentParser(description='IRKit CLI Client for Python. v{0}'.format(VERSION))

LOCAL = CMD_PARSER.add_argument_group('local')
INTERNET = CMD_PARSER.add_argument_group('internet')

base_uri = resolve_irkit_addresses()[0]
