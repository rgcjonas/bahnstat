#!/usr/bin/env python3

from bahnstat.datatypes import WatchedStop
from bahnstat.efarunner import Runner
from bahnstat.sdnotify import SystemdNotifier
from config import *

import logging
from argparse import ArgumentParser
from uuid import UUID

ap = ArgumentParser()

ap.add_argument('--db-file', required=True)
ap.add_argument('--log', default='WARN')

args = ap.parse_args()

num_loglevel = getattr(logging, args.log.upper(), None)
if not isinstance(num_loglevel, int):
    raise ValueError('Invalid log level: {}'.format(args.log))

logging.basicConfig(level=num_loglevel)

r = Runner(args.db_file, [WatchedStop(UUID(a),b,c,d) for a,b,c,d in EFA_STOPS], EFA_USER_AGENT, SystemdNotifier().watchdog)
r.run()

