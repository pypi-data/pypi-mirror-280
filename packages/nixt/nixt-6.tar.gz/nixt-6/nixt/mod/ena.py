# This file is placed in the Public Domain.


"init"


from nixt.run.main   import mods
from nixt.run.thread import launch
from nixt.run.utils  import spl


def ena(event):
    "enable a  module."
    if not mods:
        event.reply("modules are not available")
        return
    if not event.args:
        event.reply("ena <name>")
        return
    modnames = spl(event.args[0])
    for nme in modnames:
        mod = getattr(mods, nme, None)
        if "init" in dir(mod):
            event.reply(f"launched {nme}")
            launch(mod.init)
