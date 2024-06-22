# This file is placed in the Public Domain.


"uptime"


import time


from ..run.utils import laps


STARTTIME = time.time()


def upt(event):
    event.reply(laps(time.time() - STARTTIME))
