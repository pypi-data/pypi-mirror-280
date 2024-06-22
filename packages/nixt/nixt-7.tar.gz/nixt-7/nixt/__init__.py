# This file is placed in the Public Domain.


"you have been nixt."


from . import mod, usr


def getmod(name):
    print(mod)
    print(usr)
    mods = getattr(mod, name, None)
    if not mods:
        mods = getattr(usr, name, None)
    return mods
