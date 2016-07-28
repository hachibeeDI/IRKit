# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, )

from logging import getLogger
logger = getLogger(__name__)


import select
from socket import gethostbyname
from collections import deque

from . import pybonjour


REGTYPE = '_irkit._tcp'
timeout = 5
RESOLVED = []
HOST_TARGETS = deque()


def resolve_callback(
        sdRef, flags, interfaceIndex,
        errorCode, fullname, hosttarget,
        port, txtRecord):
    if errorCode == pybonjour.kDNSServiceErr_NoError:
        HOST_TARGETS.append(hosttarget)
        RESOLVED.append(True)


def browse_callback(
        sdRef, flags, interfaceIndex,
        errorCode, serviceName, regtype, replyDomain):
    if errorCode != pybonjour.kDNSServiceErr_NoError:
        return
    if not (flags & pybonjour.kDNSServiceFlagsAdd):
        return

    with pybonjour.DNSServiceResolve(
        0,
        interfaceIndex,
        serviceName,
        regtype,
        replyDomain,
        resolve_callback
    ) as resolve_sdRef:
        while not RESOLVED:
            ready = select.select([resolve_sdRef], [], [], timeout)
            if resolve_sdRef not in ready[0]:
                logger.error('Resolve timed out')
                break
            pybonjour.DNSServiceProcessResult(resolve_sdRef)
        else:
            RESOLVED.pop()


def resolve_irkit_addresses():
    with pybonjour.DNSServiceBrowse(
            regtype=REGTYPE,
            callBack=browse_callback,
    ) as browse_sdRef:
        pybonjour.DNSServiceProcessResult(browse_sdRef)
    return [gethostbyname(host) for host in HOST_TARGETS]


if __name__ == '__main__':
    hosts = resolve_irkit_addresses()
    print(hosts)
