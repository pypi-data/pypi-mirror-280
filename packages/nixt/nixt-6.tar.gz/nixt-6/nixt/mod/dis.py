# This file is placed in the Public Domain.


"disable"


from nixt.run.thread import launch
from nixt.run.main   import mods
from nixt.run.utils  import spl


def dis(event):
    "disable"
    if not mods:
        event.reply("modules are not available")
        return
    if not event.args:
        event.reply("dis <name>")
        return
    modnames = spl(event.args[0])
    for name in modnames:
        mod = getattr(mods, name, None)
        if not mod:
            continue
        if "shutdown" in dir(mod):
            event.reply(f"shutdown {name}")
            launch(mod.shutdown)
